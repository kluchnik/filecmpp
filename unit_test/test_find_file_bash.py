import pytest
import subprocess

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

@pytest.mark.parametrize('item', data_cfg)
def test_config_find(item):
    assert lib.find_file_bash.config_find(**item['in']) == item['out']

@pytest.mark.parametrize('item', data_bash)
def test_echo_null_byte(fake_process, item):
    fake_process.register_subprocess(['/bin/bash', '-c', item['in']['cmd']], stdout=item['in']['stdout'], stderr=item['in']['stderr'])
    assert lib.find_file_bash.bash(item['in']['cmd']) == item['out']

