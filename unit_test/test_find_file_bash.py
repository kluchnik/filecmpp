import pytest

import lib.find_file_bash

data_cfg = (
    {'in': {
        'directory': './',
        'extra_param': '',
        'ignore_name': '.*',
        'check_md5sum': False
        },
    'out': ('find ./  -type f -not -name ".*" -printf "%p\t%h\t%f\t%u\t%g\t%s\t%TY-%Tm-%Td %TT\t" -exec bash -c \'echo -ne "-\n";\' excec-sh {} \';\'', '')
    },
    {'in': {
        'directory': '/tmp/',
        'extra_param': '-maxdepth 1',
        'ignore_name': '.txt',
        'check_md5sum': True
        },
    'out': ('find /tmp/ -maxdepth 1 -type f -not -name ".txt" -printf "%p\t%h\t%f\t%u\t%g\t%s\t%TY-%Tm-%Td %TT\t" -exec bash -c \'md5=($(md5sum -b "$1")); echo -ne "$md5\n";\' excec-sh {} \';\'', '')
    }
    )

data_bash = (
    {
        'in': {'cmd': 'echo -ne "test-1\n"', 'stdout': 'test-1\n', 'stderr': ''},
        'out': (('test-1',), '')
    },
    {
        'in': {'cmd': 'echo -ne "test-1\ntest-2\n"', 'stdout': 'test-1\ntest-2\n', 'stderr': ''},
        'out': (('test-1', 'test-2'), '')
    },
    {
        'in': {'cmd': 'echo -ne "test-1\n\ntest-2\n"', 'stdout': 'test-1\n\ntest-2\n', 'stderr': ''},
        'out': (('test-1', 'test-2'), '')
    },
    {
        'in': {'cmd': 'echo -ne "test-1\ntest-2\n"', 'stdout': 'test-1\ntest-2\n', 'stderr': 'none\n'},
        'out': (('test-1', 'test-2'), 'Error find:\nnone\n')
    }
    )

def test_get_reference_parameters():
    assert lib.find_file_bash.get_reference_parameters(only_required=True) == ('directory', )
    assert lib.find_file_bash.get_reference_parameters(only_required=False) == ('directory', 'extra_param', 'ignore_name', 'check_md5sum')

@pytest.mark.parametrize('item', data_cfg)
def test_config_find(item):
    assert lib.find_file_bash.config_find(**item['in']) == item['out']

@pytest.mark.parametrize('item', data_bash)
def test_bash(fake_process, item):
    fake_process.register_subprocess(['/bin/bash', '-c', item['in']['cmd']], stdout=item['in']['stdout'], stderr=item['in']['stderr'])
    assert lib.find_file_bash.bash(item['in']['cmd']) == item['out']

def test_run(fake_process):
    data_in = {'directory': '/tmp', 'extra_param': '', 'ignore_name': '.*', 'check_md5sum': False}
    data_cmd = {
        'cmd': 'find /tmp  -type f -not -name ".*" -printf "%p\t%h\t%f\t%u\t%g\t%s\t%TY-%Tm-%Td %TT\t" -exec bash -c \'echo -ne "-\n";\' excec-sh {} \';\'',
        'stdout': 'test-1\ntest-2\n',
        'stderr': 'none\n'
        }
    data_out = (('test-1', 'test-2'), 'Error find:\nnone\n')
    fake_process.register_subprocess(['/bin/bash', '-c', data_cmd['cmd']], stdout=data_cmd['stdout'], stderr=data_cmd['stderr'])
    assert lib.find_file_bash.run(**data_in) == data_out