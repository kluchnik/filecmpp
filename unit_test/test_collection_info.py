import pytest

import lib.collection_info


def get_data_config():
    ''' Исходная конфигурация сканирования '''
    data = {
        'report': 'stdout', 'show_type': 'path', 'show_subtract': '', 'show_select': 'all',
        'method': 'bash',
        'extra_param': '', 'ignore_name': '.*', 'check_md5sum': False,
        'parameters': {
            'target_1': {'directory': '/tmp/1'},
            'target_2': {'directory': '/tmp/2'},
            'target_3': {'directory': '/tmp/3'}
        }
    }
    return data

def get_data_find_config():
    ''' Данные для поиска после подготовки '''
    data = {
        'target_1': {'directory': '/tmp/1',
            'extra_param': '', 'ignore_name': '.*', 'check_md5sum': False},
        'target_2': {'directory': '/tmp/2',
            'extra_param': '', 'ignore_name': '.*', 'check_md5sum': False},
        'target_3': {'directory': '/tmp/3',
            'extra_param': '', 'ignore_name': '.*', 'check_md5sum': False}
    }
    return data

def get_data_bash_cmd():
    ''' Команнды выполняемые в оболочке '''
    data = (
      {
        'cmd': 'find /tmp/1  -type f -not -name ".*" -printf "%p\t%h\t%f\t%u\t%g\t%s\t%TY-%Tm-%Td %TT\t" -exec bash -c \'echo -ne "-\n";\' excec-sh {} \';\'',
        'stdout': 'test-1\ntest-2\n', 'stderr': ''
      },
      {
        'cmd': 'find /tmp/2  -type f -not -name ".*" -printf "%p\t%h\t%f\t%u\t%g\t%s\t%TY-%Tm-%Td %TT\t" -exec bash -c \'echo -ne "-\n";\' excec-sh {} \';\'',
        'stdout': 'test-2\ntest-3\n', 'stderr': ''
      },
      {
        'cmd': 'find /tmp/3  -type f -not -name ".*" -printf "%p\t%h\t%f\t%u\t%g\t%s\t%TY-%Tm-%Td %TT\t" -exec bash -c \'echo -ne "-\n";\' excec-sh {} \';\'',
        'stdout': 'test-1\ntest-2\ntest-3\n', 'stderr': ''
      }
    )
    return data

def get_data_check():
    ''' Проверочные данные работы компонента '''
    data = {
        'target_1': {'result': ('test-1', 'test-2'), 'error': ''},
        'target_2': {'result': ('test-2', 'test-3'), 'error': ''},
        'target_3': {'result': ('test-1', 'test-2', 'test-3'), 'error': ''}
    }
    return data

def test_find_bash_pos(fake_process):
    data_config = get_data_config()
    data_find_config = get_data_find_config()
    data_bash_cmd = get_data_bash_cmd()
    data_check = get_data_check()

    for item in data_bash_cmd:
        fake_process.register_subprocess(['/bin/bash', '-c', item['cmd']], stdout=item['stdout'], stderr=item['stderr'])
    
    collection = lib.collection_info.Collection()
    
    assert collection.get_config_status()[0] == False
    assert collection.get_find_status()[0] == False
    assert collection.set_config(data_config)
    assert collection.get_config() == data_config
    assert collection.check_config()
    assert collection.get_config_status()[0] == True
    assert collection.get_find_status()[0] == False
    assert collection.get_find_module() is not None
    assert collection.get_find_config() == data_find_config
    assert collection.run()
    assert collection.get_config_status()[0] == True
    assert collection.get_find_status()[0] == True
    assert collection.get_find_result() == data_check