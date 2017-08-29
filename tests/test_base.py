from unittest.mock import Mock

import pytest

from scripts.base import BaseConfig
from scripts.data_csv import QcatDataCsv


def get_config_class(config_dict):
    config_class = type('ConfigClass', (BaseConfig,), config_dict)
    return config_class()


def get_full_url(url: str) -> str:
    return f'https://qcat.wocat.net{url}'


def test_no_config_file():
    args = Mock(config_file='foo.py')
    with pytest.raises(SystemExit):
        QcatDataCsv(args)


def test_invalid_config_file():
    args = Mock(config_file=__file__)
    with pytest.raises(SystemExit):
        QcatDataCsv(args)


def test_accepts_config_object():
    args = Mock()
    config_object = Mock()
    eqd = QcatDataCsv(arguments=args, config_object=config_object)
    assert eqd.config == config_object


def test_extract_path_simple():
    eqd = QcatDataCsv(arguments=Mock(), config_object=Mock())
    data = {
        'key_1': {
            'value': [
                {
                    'value': 'Value',
                }
            ]
        }
    }
    path = ['key_1', 'value', 'value']
    data = eqd.extract_attributes_by_path(data, path)
    assert data == [['Value']]


def test_extract_path_repeating():
    eqd = QcatDataCsv(arguments=Mock(), config_object=Mock())
    data = {
        'key_1': {
            'value': [
                {
                    'value': 'Value 1',
                },
                {
                    'value': 'Value 2'
                }
            ]
        }
    }
    path = ['key_1', 'value', 'value']
    data = eqd.extract_attributes_by_path(data, path)
    assert data == [['Value 1'], ['Value 2']]


def test_extract_path_checkbox():
    eqd = QcatDataCsv(arguments=Mock(), config_object=Mock())
    data = {
        'key_1': {
            'value': [
                {
                    'values': ['Value 1', 'Value 2'],
                }
            ]
        }
    }
    path = ['key_1', 'value', 'values']
    data = eqd.extract_attributes_by_path(data, path)
    assert data == [['Value 1', 'Value 2']]


def test_extract_path_int():
    eqd = QcatDataCsv(arguments=Mock(), config_object=Mock())
    data = {
        'key_1': {
            'value': [
                {
                    'value': 123,
                }
            ]
        }
    }
    path = ['key_1', 'value', 'value']
    data = eqd.extract_attributes_by_path(data, path)
    assert data == [['123']]


def test_extract_path_none():
    eqd = QcatDataCsv(arguments=Mock(), config_object=Mock())
    data = {}
    path = ['key_1', 'value', 'value']
    data = eqd.extract_attributes_by_path(data, path)
    assert data == [[]]


def test_extract_path_empty():
    eqd = QcatDataCsv(arguments=Mock(), config_object=Mock())
    data = {
        'key_1': {
            'value': [
                {
                    'value': None,
                }
            ]
        }
    }
    path = ['key_1', 'value', 'value']
    data = eqd.extract_attributes_by_path(data, path)
    assert data == [[]]


def test_extract_simple_attribute(api_details_1, api_list_1):
    config = {
        'qcat_attributes': [
            {
                'path': [
                    'section_general_information',
                    'children',
                    'tech__1',
                    'children',
                    'tech__1__1',
                    'children',
                    'qg_location',
                    'children',
                    'country',
                    'value',
                    'value',
                ],
                'name': 'country'
            }
        ]
    }
    eqd = QcatDataCsv(arguments=Mock(), config_object=get_config_class(config))
    mock_query = Mock()
    mock_query.return_value = api_details_1
    eqd._query = mock_query
    list_entry = api_list_1['results'][0]
    attrs = eqd.extract_attributes(list_entry)
    assert attrs == {
        'code': list_entry['code'],
        'updated': list_entry['updated'],
        'url': get_full_url(list_entry['url']),
        'country': 'Afghanistan',
    }


def test_extract_simple_attribute_none(api_details_1, api_list_1):
    config = {
        'qcat_attributes': [
            {
                'path': [
                    'section_specifications',
                    'children',
                    'tech__2',
                    'children',
                    'tech__2__6',
                    'children',
                    'tech_qg_160',
                    'children',
                    'tech_implementation_year',
                    'value',
                    'value',
                ],
                'name': 'implementation_year'
            }
        ]
    }
    eqd = QcatDataCsv(arguments=Mock(), config_object=get_config_class(config))
    mock_query = Mock()
    mock_query.return_value = api_details_1
    eqd._query = mock_query
    list_entry = api_list_1['results'][0]
    attrs = eqd.extract_attributes(list_entry)
    assert attrs == {
        'code': list_entry['code'],
        'updated': list_entry['updated'],
        'url': get_full_url(list_entry['url']),
        'implementation_year': '',
    }


def test_extract_simple_attribute_int(api_details_2, api_list_1):
    config = {
        'qcat_attributes': [
            {
                'path': [
                    'section_specifications',
                    'children',
                    'tech__2',
                    'children',
                    'tech__2__6',
                    'children',
                    'tech_qg_160',
                    'children',
                    'tech_implementation_year',
                    'value',
                    'value',
                ],
                'name': 'implementation_year'
            }
        ]
    }
    eqd = QcatDataCsv(arguments=Mock(), config_object=get_config_class(config))
    mock_query = Mock()
    mock_query.return_value = api_details_2
    eqd._query = mock_query
    list_entry = api_list_1['results'][0]
    attrs = eqd.extract_attributes(list_entry)
    assert attrs == {
        'code': list_entry['code'],
        'updated': list_entry['updated'],
        'url': get_full_url(list_entry['url']),
        'implementation_year': '2011',
    }


def test_extract_radio(api_details_1, api_list_1):
    config = {
        'qcat_attributes': [
            {
                'path': [
                    'section_specifications',
                    'children',
                    'tech__2',
                    'children',
                    'tech__2__6',
                    'children',
                    'tech_qg_160',
                    'children',
                    'tech_implementation_decades',
                    'value',
                    'values',
                ],
                'name': 'implementation_approximate'
            }
        ]
    }
    eqd = QcatDataCsv(arguments=Mock(), config_object=get_config_class(config))
    mock_query = Mock()
    mock_query.return_value = api_details_1
    eqd._query = mock_query
    list_entry = api_list_1['results'][0]
    attrs = eqd.extract_attributes(list_entry)
    assert attrs == {
        'code': list_entry['code'],
        'updated': list_entry['updated'],
        'url': get_full_url(list_entry['url']),
        'implementation_approximate': 'less than 10 years ago (recently)',
    }


def test_extract_checkbox_multiple(api_details_1, api_list_1):
    config = {
        'qcat_attributes': [
            {
                'path': [
                    'section_specifications',
                    'children',
                    'tech__3',
                    'children',
                    'tech__3__1',
                    'children',
                    'tech_qg_6',
                    'children',
                    'tech_main_purpose',
                    'value',
                    'values',
                ],
                'name': 'purpose'
            }
        ]
    }
    eqd = QcatDataCsv(arguments=Mock(), config_object=get_config_class(config))
    mock_query = Mock()
    mock_query.return_value = api_details_1
    eqd._query = mock_query
    list_entry = api_list_1['results'][0]
    attrs = eqd.extract_attributes(list_entry)
    assert attrs == {
        'code': list_entry['code'],
        'updated': list_entry['updated'],
        'url': get_full_url(list_entry['url']),
        'purpose': 'protect a watershed/ downstream areas â€“ in combination '
                   'with other Technologies|reduce risk of disasters',
    }


def test_extract_checkbox_repeating_question(api_details_2, api_list_1):
    config = {
        'qcat_attributes': [
            {
                'path': [
                    'section_specifications',
                    'children',
                    'tech__3',
                    'children',
                    'tech__3__1',
                    'children',
                    'tech_qg_6',
                    'children',
                    'tech_main_purpose',
                    'value',
                    'values',
                ],
                'name': 'purpose'
            }
        ]
    }
    eqd = QcatDataCsv(arguments=Mock(), config_object=get_config_class(config))
    mock_query = Mock()
    mock_query.return_value = api_details_2
    eqd._query = mock_query
    list_entry = api_list_1['results'][0]
    attrs = eqd.extract_attributes(list_entry)
    assert attrs == {
        'code': list_entry['code'],
        'updated': list_entry['updated'],
        'url': get_full_url(list_entry['url']),
        'purpose': 'protect a watershed/ downstream areas â€“ in combination '
                   'with other Technologies#reduce risk of disasters',
    }


def test_extract_image_checkbox(api_details_1, api_list_1):
    config = {
        'qcat_attributes': [
            {
                'path': [
                    'section_specifications',
                    'children',
                    'tech__3',
                    'children',
                    'tech__3__2',
                    'children',
                    'tech_qg_9',
                    'children',
                    'tech_landuse',
                    'value',
                    'values',
                ],
                'name': 'land_use'
            }
        ]
    }
    eqd = QcatDataCsv(arguments=Mock(), config_object=get_config_class(config))
    mock_query = Mock()
    mock_query.return_value = api_details_1
    eqd._query = mock_query
    list_entry = api_list_1['results'][0]
    attrs = eqd.extract_attributes(list_entry)
    assert attrs == {
        'code': list_entry['code'],
        'updated': list_entry['updated'],
        'url': get_full_url(list_entry['url']),
        'land_use': 'Grazing land',
    }


def test_extract_grouped_attributes(api_details_1, api_list_1):
    config = {
        'qcat_attributes': [
            {
                'grouped': [
                    {
                        'path': [
                            'section_specifications',
                            'children',
                            'tech__4',
                            'children',
                            'tech__4__5',
                            'children',
                            'tech_qg_36',
                            'children',
                            'tech_input_est_specify',
                            'value',
                            'value',
                        ]
                    },
                    {
                        'path': [
                            'section_specifications',
                            'children',
                            'tech__4',
                            'children',
                            'tech__4__5',
                            'children',
                            'tech_qg_36',
                            'children',
                            'tech_input_est_unit',
                            'value',
                            'value',
                        ]
                    }
                ],
                'name': 'costs_establishment_labour'
            }
        ]
    }
    eqd = QcatDataCsv(arguments=Mock(), config_object=get_config_class(config))
    mock_query = Mock()
    mock_query.return_value = api_details_1
    eqd._query = mock_query
    list_entry = api_list_1['results'][0]
    attrs = eqd.extract_attributes(list_entry)
    assert attrs == {
        'code': list_entry['code'],
        'updated': list_entry['updated'],
        'url': get_full_url(list_entry['url']),
        'costs_establishment_labour': 'Demarcation of the contour lines|ha#'
                                      'Excavation of the trenches and '
                                      'construction of the soil bunds|'
                                      'persons/day/ha',
    }


def test_extract_grouped_attributes_float(api_details_5):
    config = {
        'qcat_attributes': [
            {
                'grouped': [
                    {
                        'path': [
                            'section_specifications',
                            'children',
                            'tech__4',
                            'children',
                            'tech__4__5',
                            'children',
                            'tech_qg_36',
                            'children',
                            'tech_input_est_specify',
                            'value',
                            'value',
                        ]
                    },
                    {
                        'path': [
                            'section_specifications',
                            'children',
                            'tech__4',
                            'children',
                            'tech__4__5',
                            'children',
                            'tech_qg_36',
                            'children',
                            'tech_input_est_unit',
                            'value',
                            'value',
                        ]
                    }
                ],
                'name': 'costs_establishment_labour'
            }
        ]
    }
    eqd = QcatDataCsv(arguments=Mock(), config_object=get_config_class(config))
    mock_query = Mock()
    mock_query.return_value = api_details_5
    eqd._query = mock_query
    list_entry = {
        'code': '',
        'updated': '',
        'url': '',
    }
    attrs = eqd.extract_attributes(list_entry)
    assert attrs == {
        'code': list_entry['code'],
        'updated': list_entry['updated'],
        'url': get_full_url(list_entry['url']),
        'costs_establishment_labour': 'Construction|12.91',
    }


def test_extract_grouped_attributes_none(api_details_2, api_list_1):
    config = {
        'qcat_attributes': [
            {
                'grouped': [
                    {
                        'path': [
                            'section_specifications',
                            'children',
                            'tech__4',
                            'children',
                            'tech__4__5',
                            'children',
                            'tech_qg_36',
                            'children',
                            'tech_input_est_specify',
                            'value',
                            'value',
                        ]
                    },
                    {
                        'path': [
                            'section_specifications',
                            'children',
                            'tech__4',
                            'children',
                            'tech__4__5',
                            'children',
                            'tech_qg_36',
                            'children',
                            'tech_input_est_unit',
                            'value',
                            'value',
                        ]
                    }
                ],
                'name': 'costs_establishment_labour'
            }
        ]
    }
    eqd = QcatDataCsv(arguments=Mock(), config_object=get_config_class(config))
    mock_query = Mock()
    mock_query.return_value = api_details_2
    eqd._query = mock_query
    list_entry = api_list_1['results'][0]
    attrs = eqd.extract_attributes(list_entry)
    assert attrs == {
        'code': list_entry['code'],
        'updated': list_entry['updated'],
        'url': get_full_url(list_entry['url']),
        'costs_establishment_labour': '',
    }


def test_extract_grouped_attributes_partial_none(api_details_3, api_list_1):
    config = {
        'qcat_attributes': [
            {
                'grouped': [
                    {
                        'path': [
                            'section_specifications',
                            'children',
                            'tech__4',
                            'children',
                            'tech__4__5',
                            'children',
                            'tech_qg_36',
                            'children',
                            'tech_input_est_specify',
                            'value',
                            'value',
                        ]
                    },
                    {
                        'path': [
                            'section_specifications',
                            'children',
                            'tech__4',
                            'children',
                            'tech__4__5',
                            'children',
                            'tech_qg_36',
                            'children',
                            'tech_input_est_unit',
                            'value',
                            'value',
                        ]
                    }
                ],
                'name': 'costs_establishment_labour'
            }
        ]
    }
    eqd = QcatDataCsv(arguments=Mock(), config_object=get_config_class(config))
    mock_query = Mock()
    mock_query.return_value = api_details_3
    eqd._query = mock_query
    list_entry = api_list_1['results'][0]
    attrs = eqd.extract_attributes(list_entry)
    assert attrs == {
        'code': list_entry['code'],
        'updated': list_entry['updated'],
        'url': get_full_url(list_entry['url']),
        'costs_establishment_labour': 'Mano de obra|',
    }


def test_extract_grouped_attributes_partial_empty(api_details_4):
    config = {
        'qcat_attributes': [
            {
                'grouped': [
                    {
                        'path': [
                            'section_specifications',
                            'children',
                            'tech__4',
                            'children',
                            'tech__4__5',
                            'children',
                            'tech_qg_36',
                            'children',
                            'tech_input_est_specify',
                            'value',
                            'value',
                        ]
                    },
                    {
                        'path': [
                            'section_specifications',
                            'children',
                            'tech__4',
                            'children',
                            'tech__4__5',
                            'children',
                            'tech_qg_36',
                            'children',
                            'tech_input_est_unit',
                            'value',
                            'value',
                        ]
                    }
                ],
                'name': 'costs_establishment_labour'
            }
        ]
    }
    eqd = QcatDataCsv(arguments=Mock(), config_object=get_config_class(config))
    mock_query = Mock()
    mock_query.return_value = api_details_4
    eqd._query = mock_query
    list_entry = {
        'code': '',
        'updated': '',
        'url': '',
    }
    attrs = eqd.extract_attributes(list_entry)
    assert attrs == {
        'code': list_entry['code'],
        'updated': list_entry['updated'],
        'url': get_full_url(list_entry['url']),
        'costs_establishment_labour': 'Construction|#Macrophyte installation|',
    }


def test_extract_grouped_attributes_empty(api_details_2):
    config = {
        'qcat_attributes': [
            {
                'grouped': [
                    {
                        'path': [
                            'section_specifications',
                            'children',
                            'tech__4',
                            'children',
                            'tech__4__5',
                            'children',
                            'tech_qg_36',
                            'children',
                            'tech_input_est_specify',
                            'value',
                            'value',
                        ]
                    },
                    {
                        'path': [
                            'section_specifications',
                            'children',
                            'tech__4',
                            'children',
                            'tech__4__5',
                            'children',
                            'tech_qg_36',
                            'children',
                            'tech_input_est_unit',
                            'value',
                            'value',
                        ]
                    }
                ],
                'name': 'costs_establishment_labour'
            }
        ]
    }
    eqd = QcatDataCsv(arguments=Mock(), config_object=get_config_class(config))
    mock_query = Mock()
    mock_query.return_value = api_details_2
    eqd._query = mock_query
    list_entry = {
        'code': '',
        'updated': '',
        'url': '',
    }
    attrs = eqd.extract_attributes(list_entry)
    assert attrs == {
        'code': list_entry['code'],
        'updated': list_entry['updated'],
        'url': get_full_url(list_entry['url']),
        'costs_establishment_labour': '',
    }
