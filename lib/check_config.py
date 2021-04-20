'''
-------------------- Проверка и подготовка конфигурации для поиска файлов --------------------
ver.1.0
--------------------
Example-1 (Пример для bash):
    IN: <module>.run(config)
	    opts: dict config - входной словарь с параметрами для поиска:
        {
            'report': 'stdout',
            'show': 'all',
            'show_filter': '',
            'method': 'bash',
            'extra_param': '',
            'ignore_name': '.*',
            'check_md5sum': False,
            'parameters': {
                'target_1': {
                    'directory': '/tmp'
                },
                'target_2': {
                    'directory': '/tmp'
                }
            }
        }
    OUT: (status, messange, module, result)
	    opts: bool status - статус проверка
	    opts: str messange - сообщение проверки
	    opts: str module - имя модуля для поиска файлов
	    opts: dict result - выходной словарь с параметрами для поиска:
        {
            'target_1': {
                'directory': '/tmp',
                'extra_param': '',
                'ignore_name': '.*',
                'check_md5sum': False
            },
            'target_2': {
                'directory': '/tmp',
                'extra_param': '',
                'ignore_name': '.*',
                'check_md5sum': False
            }
        }

Example-2 (Пример для ssh):
    IN: <module>.run(config)
	    opts: dict config - входной словарь с параметрами для поиска:
        {
            'report': 'stdout',
            'show': 'all',
            'show_filter': '',
            'method': 'bash',
            'extra_param': '-maxdepth 1',
            'ignore_name': '.*',
            'check_md5sum': True,
            'parameters': {
                'target_1': {
                    'ip': '127.0.0.1',
                    'port': '22',
                    'username': 'user',
                    'password': '12345678',
                    'directory': '/tmp'
                },
                'target_2': {
                    'ip': '127.0.0.1',
                    'port': '22',
                    'username': 'user',
                    'password': '12345678',
                    'directory': '/tmp'
                }
        }
    OUT: (status, messange, module, result)
	    opts: bool status - статус проверка
	    opts: str messange - сообщение проверки
	    opts: str module - имя модуля для поиска файлов
	    opts: dict result - выходной словарь с параметрами для поиска:
        {
            'target_1': {
                'ip': '127.0.0.1',
                'port': '22',
                'username': 'user',
                'password': '12345678',
                'directory': '/tmp',
                'extra_param': '-maxdepth 1',
                'ignore_name': '.*',
                'check_md5sum': True
            },
            'target_2': {
                'ip': '127.0.0.1',
                'port': '22',
                'username': 'user',
                'password': '12345678',
                'directory': '/tmp',
                'extra_param': '-maxdepth 1',
                'ignore_name': '.*',
                'check_md5sum': True
            }
        }
'''

config_module = {
    'bash': 'lib.find_file_bash',
    'ssh': None,
    'test': 'lib.none'
}

def get_method_list():
    ''' Возвращает список методов '''
    return list(sorted(config_module.keys()))

def get_module(name):
    ''' Возвращает имя модуля '''
    return config_module[name]

def get_report_type():
    ''' Возвращает список допустимых значений для вывода отчета '''
    return ('stdout', )

def get_show_type():
    ''' Возвращает список допустимых значений отображения отчета '''
    return ('all', 'diff_md5sum', 'diff_size', 'diff_path', 'diff_name')

def run(config):
    ''' Запуск проверки и подготовки конфигурации '''
    status = False
    messange = 'No configuration check was performed'
    module = None
    result = None
    
    if type(config) is not dict:
        messange = 'Error: the config is not a dictionary'
        return (status, messange, module, result)

    if not 'report' in config.keys():
        messange = 'Error: missing parameter in the configuration "report"'
        return (status, messange, module, result)
    
    if not config['report'] in get_report_type():
        messange = 'Error: the report "{}" not found, use one of the " {} "'.format(config['report'], ' | '.join(get_report_type()))
        return (status, messange, module, result)

    if not 'show' in config.keys():
        messange = 'Error: missing parameter in the configuration "show"'
        return (status, messange, module, result)
    
    if not config['show'] in get_show_type():
        messange = 'Error: the show "{}" not found, use one of the " {} "'.format(config['show'], ' | '.join(get_show_type()))
        return (status, messange, module, result)

    if not 'method' in config.keys():
        messange = 'Error: missing parameter in the configuration "method"'
        return (status, messange, module, result)
    
    if not config['method'] in get_method_list():
        messange = 'Error: the method "{}" not found, use one of the " {} "'.format(config['method'], ' | '.join(get_method_list()))
        return (status, messange, module, result)
    
    exec_cmd = 'import {}'.format(get_module(config['method']))
    try:
        exec(exec_cmd)
        module = get_module(config['method'])
    except:
        messange = 'Error: import module {}'.format(get_module(config['method']))
        return (status, messange, module, result)

    if not 'get_reference_parameters' in eval('dir({})'.format(module)):
        messange = 'Error: method "get_reference_parameters" not found in the module {}'.format(get_module(config['method']))
        return (status, messange, module, result)
    
    exec_cmd = '{}.{}'.format(module, 'get_reference_parameters()')
    try:
        reference_parameters = eval(exec_cmd)
    except:
        messange = 'Error: reference parameters method {}'.format(exec_cmd)
        return (status, messange, module, result)
    
    exec_cmd = '{}.{}'.format(module, 'get_reference_parameters(False)')
    try:
        reference_parameters_all = eval(exec_cmd)
    except:
        reference_parameters_all = reference_parameters

    if not 'run' in eval('dir({})'.format(module)):
        messange = 'Error: method "run" not found in the module {}'.format(get_module(config['method']))
        return (status, messange, module, result)

    if not 'parameters' in config.keys():
        messange = 'Error: missing parameter in the configuration "parameters"'
        return (status, messange, module, result)
    
    if type(config['parameters']) is not dict:
        messange = 'Error: the config["parameters"] is not a dictionary'
        return (status, messange, module, result)

    if len(config['parameters'].keys()) == 0:
        messange = 'Error: the parameter dictionary is empty'
        return (status, messange, module, result)

    for target in config['parameters'].keys():
        if type(config['parameters'][target]) is not dict:
            messange = 'Error: the config["parameters"]["{}"] is not a dictionary'.format(target)
            return (status, messange, module, result)

    for target in config['parameters'].keys():
        for item in reference_parameters:
            if not item in config['parameters'][target].keys():
                messange = 'Error: the {} reference parameters "{}" not found'.format(target, item)
                return (status, messange, module, result)

    status = True
    messange = 'Verification was successful'
    result = {}
    for target in config['parameters'].keys():
        result[target] = {}
        for item in config.keys():
            if item in reference_parameters_all:
                result[target][item] = config[item]
        for item in config['parameters'][target].keys():
            if item in reference_parameters_all:
                result[target][item] = config['parameters'][target][item]
    
    return (status, messange, module, result)