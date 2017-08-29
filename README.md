# QCAT API Scripts


A collection of scripts to query and process data from the [QCAT API]. The scripts are used to create output files containing selected attributes of the questionnaires from the QCAT API. 

The scripts store the update timestamp of the returned questionnaires. If run repeatedly (e.g. every day or week), only modified or new questionnaires will be updated, resulting in less queries to the API. 

More information on the API can be found in the [QCAT Documentation].


## Installation

**It is recommended to install the scripts within a [virtual environment].**

*The scripts require Python 3.6 to run.*

1. (recommended) Set up and activate a [virtual environment] with Python 3.6.
1. Clone this repository.
1. Install the requirements:
        
        (env)$ pip install requirements/requirements.txt


## API Token

For queries to the [QCAT API], you will need to provide an authorization token. See the [QCAT Documentation] on [how to obtain an authorization token] 

When running the scripts, you can either pass the token as parameter (`-t <token>` or `--token <token>`) when calling the script:

        (env)$ python qcat_data_csv.py config/<config_file.py> -t <token> 

Or you can specify the token in the configuration file (see below).


## Configuration

Configuration files are Python files which need to be placed in the `config` directory. The file must contains a dictionary called `config`.

Each `config` dictionary must contain the following keys:

#### Mandatory configuration

* `api_token`: If not passed as parameter when calling the script, the API token needs to be specified as string in the configuration.

* `qcat_attributes`: A list of attributes to extract from the API data must be specified. This must be a list of dictionaries, each dictionary containing the `path` to the wanted value and a `name` for the attribute in the output file.

    Most attributes are specific to a certain type of SLM Data (e.g. SLM Technologies or SLM Approaches). Set the `api_filter_params`accordingly to avoid empty data.

    Example to extract the `name` attribute of Technologies questionnaires:
    
    ```python
  config = {
        # ...
        'qcat_attributes': [
            {
                'path': [
                    'section_general_information',
                    'children',
                    'tech__1',
                    'children',
                    'tech__1__1',
                    'children',
                    'qg_name',
                    'children',
                    'name',
                    'value',
                    'value',
                ],
                'name': 'technologies_name'
            }
        ]
    }
    ```
 
#### Optional configuration
     
* `api_filter_params` (*optional* - default: `'''`): An optional string acting as filter. You can use the same filter parameters as in the [QCAT Search View] or in the [QCAT Filter View]. The filter parameters are in the URL after the `?` and can be copied as such, just make sure to remove the `page=X` parameter if present.

    Examples:
    
    Filter the results to contain only SLM Technologies:
    
    ```python
  config = {
      # ...
      'api_filter_params': '?type=technologies'
  }
    ```
    Filter the results to contain only SLM Technologies from country Tajikistan:
    
  ```python
  config = {
    # ...
    'api_filter_params': '?type=technologies&filter__qg_location__country=country_TJK'
  }
  ```

* `output_file` (*optional* - default: `'qcat_data.csv'`): An optional name of the output file which will be created within the `output` folder. If the script runs repeatedly, the same output file is used to check for existing and unmodified questionnaires before updating the data.

* `query_limit` (*optional* - default: `None`): An optional integer to limit the query results. This is especially useful for testing the configuration.

#### Examples

There are samples in the `config` folder, which you can use to get started (rename `*.py.sample` to `*.py` and adapt as you like).


## Usage

The basic usage of the scripts are as follows:

* Query API and save data as **CSV**:

        (env)$ python qcat_data_csv.py config/<config_file>.py
        
* Query API and save data as **Geojson**:

        (env)$ python qcat_data_geojson.py config/<config_file>.py

This will create the resulting files in the `output` directory.


#### Parameters

* `config_file`: The relative path (usually in `config/` directory) to a configuration file.

* `-v` or `--verbose` (*optional*): Increase verbosity of the output

* `-t` or `--token` (*optional*): The QCAT API Token. This can be also specified in the configuration file.

* `-u` or `--update` (*optional*): Enforce updating all entries in the previous output file instead of using timestamp to update only the modified questionnaires.


## Further steps

* Cron job: The script is written to be run repeatedly (updating only new and modified attributes). You could set up a cron job to run the script automatically (e.g. every day or week). 


[QCAT API]: https://qcat.wocat.net/en/api/
[QCAT Documentation]: https://qcat.readthedocs.io/en/latest/api/docs.html
[virtual environment]: http://docs.python-guide.org/en/latest/dev/virtualenvs/
[how to obtain an authorization token]: http://qcat.readthedocs.io/en/latest/api/v2.html#authorization
[QCAT Search View]: https://qcat.wocat.net/en/wocat/list/
[QCAT Filter View]: https://qcat.wocat.net/en/wocat/filter/?type=technologies
