import sys
import pytest

data_modules = (
    'config',
    'filecmpp',
    'lib.find_file_bash',
    'lib.collection_info'
    )

@pytest.mark.parametrize('item', data_modules)
def test_modules(item):
    status = False
    try:
        exec('import {}'.format(item))
        status = True
    except Exception as exc:
        exc_type, exc_obj, _ = sys.exc_info()
        print('Error modules:\n{}: {}'.format(exc_type.__name__, exc_obj))
        status = False
    assert status == True
