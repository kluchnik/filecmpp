import pytest

import lib.collection_info

test_cases = (
    {
       'description': 'Значение по умолчанию для config',
       'setup': '',
       'set': '',
       'get': 'collection.get_config()',
       'expectations': {}
    },
    {
       'description': 'Значение по умолчанию для config_status',
       'setup': '',
       'set': '',
       'get': 'collection.get_config_status()',
       'expectations': (False, 'No configuration check was performed')
    },
    {
       'description': 'Значение по умолчанию для file_list',
       'setup': '',
       'set': '',
       'get': 'collection.get_file_list()',
       'expectations': {}
    },
    {
       'description': 'Провека метода set_config()',
       'setup': '',
       'set': "collection.set_config({'method': 'bash', 'parameters': {'pc':{'directory': '/tmp'}}})",
       'get': 'collection.get_config_status()',
       'expectations': (True, 'Verification was successful')
    },
    {
       'description': 'Провека метода set_config()',
       'setup': '',
       'set': "collection.set_config({'method': 'bash', \
'parameters': {'pc':{'directory': '/tmp', 'extra_param': '', 'ignore_name': '.*', 'check_md5sum': False}}})",
       'get': 'collection.get_config_status()',
       'expectations': (True, 'Verification was successful')
    },
    {
       'description': 'Провека метода clear_config()',
       'setup': "collection.set_config({'method': 'bash', 'parameters': {'pc':{'directory': '/tmp'}}})",
       'set': 'collection.clear_config()',
       'get': 'collection.get_config()',
       'expectations': {}
    }
    )

@pytest.mark.parametrize('item', test_cases)
def test_modules(item):
	collection = lib.collection_info.Collection()
	print(item['description'])
	exec(item['setup'])
	exec(item['set'])
	result = eval(item['get'])
	assert result == item['expectations']