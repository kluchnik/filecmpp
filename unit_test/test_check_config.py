import pytest

import lib.check_config

test_cases = (
    {
       'description': 'Проверка метода lib.check_config.run() - negative',
       'config': '',
       'expectations': (False, 'Error: the config is not a dictionary', None, None)
    },
    {
       'description': 'Проверка метода lib.check_config.run() - negative',
       'config': [],
       'expectations': (False, 'Error: the config is not a dictionary', None, None)
    },
    {
       'description': 'Проверка метода lib.check_config.run() - negative',
       'config': {},
       'expectations': (False, 'Error: missing parameter in the configuration "report"', None, None)
    },
    {
       'description': 'Проверка метода lib.check_config.run() - negative',
       'config': {'report': None},
       'expectations': (False, 'Error: the report "None" not found, use one of the " {} "'.format(' | '.join(lib.check_config.get_report_type())), None, None)
    },
    {
       'description': 'Проверка метода lib.check_config.run() - negative',
       'config': {'report': 'stdout'},
       'expectations': (False, 'Error: missing parameter in the configuration "show"', None, None)
    },
    {
       'description': 'Проверка метода lib.check_config.run() - negative',
       'config': {'report': 'stdout', 'show': None},
       'expectations': (False, 'Error: the show "None" not found, use one of the " {} "'.format(' | '.join(lib.check_config.get_show_type())), None, None)
    },
    {
       'description': 'Проверка метода lib.check_config.run() - negative',
       'config': {'report': 'stdout', 'show': 'all'},
       'expectations': (False, 'Error: missing parameter in the configuration "method"', None, None)
    },
    {
       'description': 'Проверка метода lib.check_config.run() - negative',
       'config': {'report': 'stdout', 'show': 'all', 'method': None},
       'expectations': (False, 'Error: the method "None" not found, use one of the " {} "'.format(' | '.join(lib.check_config.get_method_list())), None, None)
    },
    {
       'description': 'Проверка метода lib.check_config.run() - negative',
       'config': {'report': 'stdout', 'show': 'all', 'method': 'test'},
       'expectations': (False, 'Error: import module lib.none', None, None)
    },
    {
       'description': 'Проверка метода lib.check_config.run() - negative',
       'config': {'report': 'stdout', 'show': 'all', 'method': 'bash'},
       'expectations': (False, 'Error: missing parameter in the configuration "parameters"', '{}'.format(lib.check_config.get_module('bash')), None)
    },
    {
       'description': 'Проверка метода lib.check_config.run() - negative',
       'config': {'report': 'stdout', 'show': 'all', 'method': 'bash', 'parameters': ''},
       'expectations': (False, 'Error: the config["parameters"] is not a dictionary', '{}'.format(lib.check_config.get_module('bash')), None)
    },
    {
       'description': 'Проверка метода lib.check_config.run() - negative',
       'config': {'report': 'stdout', 'show': 'all', 'method': 'bash', 'parameters': []},
       'expectations': (False, 'Error: the config["parameters"] is not a dictionary', '{}'.format(lib.check_config.get_module('bash')), None)
    },
    {
       'description': 'Проверка метода lib.check_config.run() - negative',
       'config': {'report': 'stdout', 'show': 'all', 'method': 'bash', 'parameters': {}},
       'expectations': (False, 'Error: the parameter dictionary is empty', '{}'.format(lib.check_config.get_module('bash')), None)
    },
    {
       'description': 'Проверка метода lib.check_config.run() - negative',
       'config': {'report': 'stdout', 'show': 'all', 'method': 'bash', 'parameters': {'target_1': ''}},
       'expectations': (False, 'Error: the config["parameters"]["target_1"] is not a dictionary', '{}'.format(lib.check_config.get_module('bash')), None)
    },
    {
       'description': 'Проверка метода lib.check_config.run() - negative',
       'config': {'report': 'stdout', 'show': 'all', 'method': 'bash', 'parameters': {'target_1': []}},
       'expectations': (False, 'Error: the config["parameters"]["target_1"] is not a dictionary', '{}'.format(lib.check_config.get_module('bash')), None)
    },
    {
       'description': 'Проверка метода lib.check_config.run() - negative',
       'config': {'report': 'stdout', 'show': 'all', 'method': 'bash', 'parameters': {'target_1': {}}},
       'expectations': (False, 'Error: the target_1 reference parameters "directory" not found', '{}'.format(lib.check_config.get_module('bash')), None)
    },
    {
       'description': 'Проверка метода lib.check_config.run() - negative',
       'config': {'report': 'stdout', 'show': 'all', 'method': 'bash', 'parameters': {'target_1': {'test': None}}},
       'expectations': (False, 'Error: the target_1 reference parameters "directory" not found', '{}'.format(lib.check_config.get_module('bash')), None)
    },
    {
       'description': 'Проверка метода lib.check_config.run() - possitive',
       'config': {'report': 'stdout', 'show': 'all', 'method': 'bash', 'parameters': {'target_1': {'test': None, 'directory': '/tmp'}}},
       'expectations': (True, 'Verification was successful', '{}'.format(lib.check_config.get_module('bash')), {'target_1': {'directory': '/tmp'}})
    },
    {
       'description': 'Проверка метода lib.check_config.run() - possitive',
       'config': {
           'report': 'stdout', 'show': 'all', 'method': 'bash',
           'parameters': {'target_1': {'directory': '/tmp/1'}, 'target_2': {'directory': '/tmp/2'}}
           },
       'expectations': (True, 'Verification was successful', '{}'.format(lib.check_config.get_module('bash')), 
       	{'target_1': {'directory': '/tmp/1'}, 'target_2': {'directory': '/tmp/2'}})
    },
    {
       'description': 'Проверка метода lib.check_config.run() - possitive',
       'config': {
           'report': 'stdout', 'show': 'all', 'method': 'bash',
           'extra_param': '-maxdepth 1',
           'parameters': {'target_1': {'test': None, 'directory': '/tmp'}}
           },
       'expectations': (True, 'Verification was successful', '{}'.format(lib.check_config.get_module('bash')),
       	{'target_1': {'directory': '/tmp', 'extra_param': '-maxdepth 1'}})
    },
    {
       'description': 'Проверка метода lib.check_config.run() - possitive',
       'config': {
           'report': 'stdout', 'show': 'all', 'method': 'bash',
           'ignore_name': '.*',
           'parameters': {'target_1': {'test': None, 'directory': '/tmp'}}
           },
       'expectations': (True, 'Verification was successful', '{}'.format(lib.check_config.get_module('bash')),
       	{'target_1': {'directory': '/tmp', 'ignore_name': '.*'}})
    },
    {
       'description': 'Проверка метода lib.check_config.run() - possitive',
       'config': {
           'report': 'stdout', 'show': 'all', 'method': 'bash',
           'check_md5sum': True,
           'parameters': {'target_1': {'test': None, 'directory': '/tmp'}}
           },
       'expectations': (True, 'Verification was successful', '{}'.format(lib.check_config.get_module('bash')),
       	{'target_1': {'directory': '/tmp', 'check_md5sum': True}})
    },
    {
       'description': 'Проверка метода lib.check_config.run() - possitive',
       'config': {
           'report': 'stdout', 'show': 'all', 'method': 'bash',
           'extra_param': '-maxdepth 1',
           'ignore_name': '.*',
           'check_md5sum': True,
           'test': None,
           'parameters': {'target_1': {'test': None, 'directory': '/tmp/1'}, 'target_2': {'test': None, 'directory': '/tmp/2'}}
           },
       'expectations': (True, 'Verification was successful', '{}'.format(lib.check_config.get_module('bash')),
       	{
           'target_1': {'directory': '/tmp/1', 'extra_param': '-maxdepth 1', 'ignore_name': '.*', 'check_md5sum': True},
           'target_2': {'directory': '/tmp/2', 'extra_param': '-maxdepth 1', 'ignore_name': '.*', 'check_md5sum': True},
       	})
    }
    )

@pytest.mark.parametrize('item', test_cases)
def test_modules(item):
	print(item['description'])
	config = item['config']
	assert lib.check_config.run(config) == item['expectations']