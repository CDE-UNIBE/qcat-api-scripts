import importlib.util
import os
import requests
import sys

from argparse import ArgumentParser
from datetime import datetime

from tqdm import tqdm


class BaseConfig:

    # Required - must be set in config file
    api_token = ''
    qcat_attributes = []

    # Optional - can be overwritten in config file
    qcat_base_url = 'https://qcat.wocat.net'
    api_filter_params = ''
    query_limit = None
    output_file = 'qcat_data.csv'
    question_separator = '|'
    row_separator = '#'


class ArgParser:

    def __init__(self, description):
        self.parser = ArgumentParser(
            description=description)

        self.parser.add_argument(
            'config_file',
            help='Relative path to a configuration file. See samples.')

        self.parser.add_argument(
            '-v', '--verbose', help='Increase output verbosity',
            action='store_true')

        self.parser.add_argument(
            '-t', '--token', help='QCAT API Token', action='store')

        self.parser.add_argument(
            '-u', '--update',
            help='Enforce update of ALL entries of previous output file',
            action='store_true')

    def parse(self):
        return self.parser.parse_args()


class QcatApiMixin:

    def __init__(self, arguments, config_object=None):
        self.args = arguments

        if config_object is None:
            # Try to load the configuration file
            spec = importlib.util.spec_from_file_location(
                'config', self.args.config_file)
            mod = importlib.util.module_from_spec(spec)
            try:
                spec.loader.exec_module(mod)
            except FileNotFoundError:
                self.error(
                    'Config file "{config_file}" was not found.'.format(
                        config_file=self.args.config_file))

            try:
                self.config_dict = mod.config
            except AttributeError:
                self.error(
                    'Config file "{config_file}" is not valid. It needs to '
                    'contains a dict "config"'.format(
                        config_file=self.args.config_file))

            # If token was provided as an argument, set it
            if self.args.token:
                self.config_dict['api_token'] = self.args.token

            for required in ['api_token', 'qcat_attributes']:
                if required not in self.config_dict \
                        or not self.config_dict[required]:
                    self.error(
                        '"{required}" must be specified in the configuration. '
                        'See the Readme file for more information.'.format(
                            required=required))

            config_class = type('ConfigClass', (BaseConfig,), self.config_dict)

            self.config = config_class()
        else:
            # Configuration file was provided, use this
            self.config = config_object

        # Use a request session for "keep-alive" of the connection
        self.session = requests.Session()
        self.session.headers.update({
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Token {api_token}'.format(
                api_token=self.config.api_token)
            })

    def handle(self):
        """The main function, extracts the data."""

        remote_questionnaires = self.query_questionnaires(
            [], self._get_request_url('questionnaires/'))

        local_questionnaires = self.read_data()

        if self.args.update:
            print('Update option is set, ignoring existing entries in '
                  'attribute file.')
            local_questionnaires = []

        self.check_local_questionnaires(local_questionnaires)

        questionnaires = self.update_questionnaires(
            remote_questionnaires, local_questionnaires)

        self.write_data(questionnaires)

    def query_questionnaires(self, results: list, url: str) -> list:
        """Query questionnaires recursively."""

        if not results:
            self.log('Querying questionnaires ...')

        self.log('... Querying {url}'.format(url=url))

        query = self._query(url)
        if query is None:
            # API limit hit
            sys.exit()

        results.extend(query.get('results', []))

        if self.config.query_limit and len(results) > self.config.query_limit:
            subset = results[:self.config.query_limit]
            self.log('Query limit set, returning subset of results.')
            print('Fetched {len_subset} questionnaires.'.format(
                len_subset=len(subset)))
            return subset

        # If there are more questionnaires, query the next page
        next_url = query.get('next')
        if next_url:
            return self.query_questionnaires(results, next_url)

        print('Fetched {len_results} questionnaires.'.format(
            len_results=len(results)))

        return results

    def log(self, msg: str) -> None:
        """Log verbose output if desired."""
        if self.args.verbose:
            print(msg)

    @staticmethod
    def error(msg: str) -> None:
        """Show the error message and exit."""
        print('ERROR: {msg}'.format(msg=msg))
        sys.exit()

    def check_local_questionnaires(self, questionnaires: list) -> None:
        # Override if needed
        pass

    def write_data(self, data: list) -> None:
        raise NotImplementedError()

    def read_data(self) -> list:
        raise NotImplementedError()

    def update_questionnaires(
            self, remote_questionnaires: list,
            local_questionnaires: list) -> list:
        """
        Update the questionnaires. No need to fetch details of local
        questionnaires which have not been updated.
        """

        # Check which questionnaires to ignore, update or add.
        untouched_questionnaires = []
        updated_questionnaires = []
        new_questionnaires = []
        for remote in remote_questionnaires:
            code = remote['code']
            remote_updated = self._parse_time(remote['updated'])
            local_questionnaire = next(
                (item for item in local_questionnaires if item['code'] == code),
                None)
            if local_questionnaire:
                # Remote questionnaire exists in local list
                local_updated = self._parse_time(local_questionnaire['updated'])
                if remote_updated > local_updated:
                    # Remote questionnaire has been updated, get new attributes
                    updated_questionnaires.append(remote)
                else:
                    # Remote questionnaire did not change, keep same attributes
                    untouched_questionnaires.append(local_questionnaire)
            else:
                # Remote questionnaire does not exist in local list
                new_questionnaires.append(remote)

        # Questionnaires in local but not untouched or updated will be removed.
        # Get count, just for display.
        removed_questionnaire_count = max(
            len(local_questionnaires) - len(untouched_questionnaires) -
            len(updated_questionnaires), 0)

        print('{len_untouched_questionnaires} entries still up to date, '
              '{len_updated_questionnaires} will be updated, '
              '{len_new_questionnaires} will be newly added, '
              '{removed_questionnaire_count} entries will be removed.'.format(
                len_untouched_questionnaires=len(untouched_questionnaires),
                len_updated_questionnaires=len(updated_questionnaires),
                len_new_questionnaires=len(new_questionnaires),
                removed_questionnaire_count=removed_questionnaire_count))

        limit_hit = False

        # Get details of updated questionnaires
        write_questionnaires = untouched_questionnaires
        if updated_questionnaires:
            self.log('... Fetching attributes of {len_updated_questionnaires} '
                     'updated entries.'.format(
                len_updated_questionnaires=len(updated_questionnaires)))
            updated_attrs, limit_hit = self.get_attributes(
                updated_questionnaires)
            if limit_hit is True:
                self.log('... Only updated {len_updated_attrs} entries because '
                         'of API limit.'.format(
                    len_updated_attrs=len(updated_attrs)))
            write_questionnaires.extend(updated_attrs)

        # Get details of new questionnaires
        if new_questionnaires:
            if limit_hit is True:
                self.log('... Not adding new entries because of API limit.')
            else:
                self.log('... Fetching attributes of {len_new_questionnaires} '
                         'new entries.'.format(
                    len_new_questionnaires=len(new_questionnaires)))
                new_attrs, limit_hit = self.get_attributes(new_questionnaires)
                if limit_hit is True:
                    self.log('... Only added {len_new_attrs} entries because of'
                             ' API limit.'.format(len_new_attrs=len(new_attrs)))
                write_questionnaires.extend(new_attrs)

        return write_questionnaires

    def get_attributes(self, questionnaire_list: list) -> (list, bool):
        """Get the attributes of a list of questionnaires."""
        return_list = []
        limit_hit = False
        for q in tqdm(questionnaire_list, desc='queries', unit='q',
                      disable=not self.args.verbose):
            if limit_hit is False:
                attrs = self.extract_attributes(q)
                if attrs is None:
                    limit_hit = True
                else:
                    return_list.append(attrs)
        return return_list, limit_hit

    def extract_attributes(self, list_entry: dict) -> dict or None:
        """
        Get the attributes of a single questionnaire by querying its details
        over the API. If None is returned, the API limit was hit.
        """
        # Query details
        url = '{qcat_base_url}/en/api/v2/questionnaires/{code}/'.format(
            qcat_base_url=self.config.qcat_base_url, code=list_entry['code'])

        query = self._query(url)
        if query is None:
            # API limit hit
            return None

        attributes = self._get_basic_attributes(list_entry)

        for attr in self.config.qcat_attributes:
            if 'grouped' in attr:
                # Grouped attributes, get each path separately
                group_data = []
                for grouped_attr in attr['grouped']:
                    data = self.extract_attributes_by_path(
                        query, grouped_attr['path'])
                    group_data.append(data)

                # Regroup them into rows.
                row_data = list(zip(*group_data))

                # Flatten the list and add empty values
                flattened_rows = []
                for row in row_data:
                    flat_row = []
                    for question_group in row:
                        if not question_group:
                            question_group = ['']
                        flat_row.extend(question_group)
                    flattened_rows.append(flat_row)

                # Join fields values to rows
                row_values = [
                    self.config.question_separator.join(row) for row in
                    flattened_rows]

                # Join the rows to a single value
                row_value = self.config.row_separator.join(row_values)

                # Finally, if the row only consists of separators, set it
                # "empty" manually
                if row_value.replace(
                        self.config.question_separator, '').replace(
                        self.config.row_separator, '') == '':
                    row_value = ''

                attributes[attr['name']] = row_value

            else:
                # Ungrouped attribute
                extracted_rows = self.extract_attributes_by_path(
                    query, attr['path'])

                row_values = []
                for row in extracted_rows:
                    values = []
                    if isinstance(row, list):
                        for val in row:
                            if isinstance(val, list):
                                # Image checkbox
                                values.append(str(val[0]))
                            else:
                                values.append(str(val))
                    else:
                        values.append(str(row))
                    row_values.append(
                        self.config.question_separator.join(values))
                attributes[attr['name']] = self.config.row_separator.join(
                    row_values)

        return attributes

    def extract_attributes_by_path(self, data: dict, path: list) -> list:
        """
        Extract one or more attributes by walking down the specified path.
        Always return a nested list of values.

        See tests for examples.
        """
        data_part = data.get(path[0])
        if not data_part:
            if len(path) > 1:
                # Was not able to reach final element, return empty.
                return [[]]
            else:
                # Final element is not available or None.
                return []

        if len(path) == 1:
            # Last element
            if not isinstance(data_part, list):
                # Turn into list if it is not already.
                return [str(data_part)]
            else:
                return data_part

        if isinstance(data_part, dict):
            # Drill down further along the path
            return self.extract_attributes_by_path(data_part, path[1:])

        elif isinstance(data_part, list):
            # (Repeating) question
            repeating_data = []
            for repeating in data_part:
                question_data = self.extract_attributes_by_path(
                    repeating, path[1:])
                repeating_data.append(question_data)
            return repeating_data

        else:
            raise Exception(
                'data_part should be either list or dict: {data_part}'.format(
                    data_part=data_part))

    def get_output_file_path(self):
        return os.path.join('output', self.config.output_file)

    def _get_basic_attributes(self, list_entry: dict) -> dict:
        """
        Return the basic attributes available for each questionnaire entry in
        the CSV.
        """
        return {
            'code': list_entry.get('code'),
            'updated': list_entry.get('updated'),
            'url': '{qcat_base_url}{list_entry_url}'.format(
                qcat_base_url=self.config.qcat_base_url,
                list_entry_url=list_entry.get("url")),
        }

    @staticmethod
    def _parse_time(time_string: str) -> datetime:
        """Parse a time from string."""

        # Strings with timezone (+01:00) in v2 are not easily parsed. But time
        # zones are not important here, so we just omit them.
        time_string = time_string.rsplit('+')[0]

        time_formats = [
            '%Y-%m-%dT%H:%M:%S.%fZ',  # Default
            '%Y-%m-%dT%H:%M:%SZ',  # Imported UNCCD data
            '%Y-%m-%dT%H:%M:%S.%f',  # Stripped timezone format (v2)
        ]
        for t_format in time_formats:
            try:
                return datetime.strptime(time_string, t_format)
            except ValueError:
                continue

    def _query(self, url: str):
        """Query the API"""
        r = self.session.get(url)
        if r.status_code == 429:
            # Too many requests, API limit was hit
            print('You seem to have hit the limit of daily API calls. Please '
                  'run the script again the next day to extract the remaining '
                  'data.')
            return None
        if not r.ok:
            self.error(
                'Error fetching data. Query to API returned status '
                '{status_code} ({reason})'.format(
                    status_code=r.status_code, reason=r.reason))
        return r.json()

    def _get_request_url(self, endpoint: str) -> str:
        """Put together API URL"""
        return '{qcat_base_url}/en/api/v2/{endpoint}{filter_params}'.format(
            qcat_base_url=self.config.qcat_base_url, endpoint=endpoint,
            filter_params=self.config.api_filter_params)

