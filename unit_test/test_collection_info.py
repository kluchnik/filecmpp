import pytest

import lib.collection_info

def test_possitive(fake_process):
    data_config = {
        'report': 'stdout',
        'show': 'all',
        'show_filter': '',
        'method': 'bash',
        'extra_param': '',
        'ignore_name': '.*',
        'check_md5sum': False,
        'parameters': {
            'target_1': {
                'directory': '/tmp/1'
            },
            'target_2': {
                'directory': '/tmp/2'
            }
        }
    }

    data_find_config = {
        'target_1': {
            'directory': '/tmp/1',
            'extra_param': '',
            'ignore_name': '.*',
            'check_md5sum': False
        },
        'target_2': {
            'directory': '/tmp/2',
            'extra_param': '',
            'ignore_name': '.*',
            'check_md5sum': False
        }
    }

    data_cmd_1 = {
        'cmd': 'find /tmp/1  -type f -not -name ".*" -printf "%p\t%h\t%f\t%u\t%g\t%s\t%TY-%Tm-%Td %TT\t" -exec bash -c \'echo -ne "-\n";\' excec-sh {} \';\'',
        'stdout': 'test-1\ntest-2\n',
        'stderr': ''
        }

    data_cmd_2 = {
        'cmd': 'find /tmp/2  -type f -not -name ".*" -printf "%p\t%h\t%f\t%u\t%g\t%s\t%TY-%Tm-%Td %TT\t" -exec bash -c \'echo -ne "-\n";\' excec-sh {} \';\'',
        'stdout': 'test-2\ntest-3\n',
        'stderr': ''
        }

    data_out = {
        'target_1': {
            'result': ('test-1', 'test-2'),
            'error': ''
        },
        'target_2': {
            'result': ('test-2', 'test-3'),
            'error': ''
        }
    }
    fake_process.register_subprocess(['/bin/bash', '-c', data_cmd_1['cmd']], stdout=data_cmd_1['stdout'], stderr=data_cmd_1['stderr'])
    fake_process.register_subprocess(['/bin/bash', '-c', data_cmd_2['cmd']], stdout=data_cmd_2['stdout'], stderr=data_cmd_2['stderr'])
    
    collection = lib.collection_info.Collection()
    collection.set_config(data_config)
    collection.check_config()
    assert collection.get_config_status()[0] == True
    assert collection.get_find_module() is not None
    assert collection.get_find_config() == data_find_config
    collection.run()
    assert collection.get_find_result() == data_out