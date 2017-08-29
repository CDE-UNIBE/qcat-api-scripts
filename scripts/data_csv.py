import csv

from scripts.base import QcatApiMixin


class QcatDataCsv(QcatApiMixin):
    """
    Store QCAT API data as CSV.
    """

    def check_local_questionnaires(self, local_questionnaires):
        if local_questionnaires:
            # Sanity check
            self._check_attribute_length(local_questionnaires[0])

    def read_data(self) -> list:
        """Read a local CSV file"""
        rows = []
        output_file = self.get_output_file_path()
        try:
            with open(output_file, newline='') as csv_file:
                reader = csv.DictReader(csv_file, **self._get_csv_options())
                for row in reader:
                    rows.append(row)
            self.log(f'Found existing attribute file "{output_file}" with '
                     f'{len(rows)} entries.')
        except FileNotFoundError:
            self.log('No existing attribute file found.')
        return rows

    def write_data(self, data: list) -> None:
        """Write a local CSV file"""
        try:
            fieldnames = data[0].keys()
        except IndexError:
            fieldnames = []
        output_file = self.get_output_file_path()
        with open(output_file, 'w', newline='') as csv_file:
            writer = csv.DictWriter(
                csv_file, fieldnames=fieldnames, **self._get_csv_options())
            writer.writeheader()
            for row in data:
                writer.writerow(row)
        print(f'Output file "{output_file}" written.')

    @staticmethod
    def _get_csv_options() -> dict:
        """Options for CSV writing and reading"""
        return {'delimiter': ';', 'quoting': csv.QUOTE_NONNUMERIC}

    def _check_attribute_length(self, local_questionnaire: dict):
        """
        Small sanity check: If number of attributes in local file does not match
        those in configuration, return.
        """
        if len(self._get_basic_attributes({})) + \
                len(self.config.qcat_attributes) != \
                len(local_questionnaire):
            qcat_attributes_length = len(self._get_basic_attributes({})) + \
                              len(self.config.qcat_attributes)
            self.error(
                f'Number of attributes ({len(local_questionnaire)}) in the '
                f'local file "{self.get_output_file_path()}" does not match '
                f'number of qcat_attributes ({qcat_attributes_length}) set in '
                f'the configuration file. Please adjust configuration or '
                f'delete previous output file.')
