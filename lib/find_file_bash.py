'''
-------------------- Модуль для поиска файлов через оболочку bash --------------------
ver.1.1
Пример использования:
--------------------
import find_file_bash

result, error = find_file_bash.run(directory='/tmp')
print('result:\\n{}\\nerror:\\n{}',format(result, error))
find_file_bash.run(directory='/tmp', extra_param='-maxdepth 1', ignore_name='*.txt', check_md5sum=True)
print('result:\\n{}\\nerror:\\n{}',format(result, error))
parameters = {'directory': '/tmp', 'extra_param': '-maxdepth 1', 'ignore_name': '*.txt', 'check_md5sum': True}
find_file_bash.run(*parameters)
print('result:\\n{}\\nerror:\\n{}',format(result, error))

--------------------
'''

import sys
import subprocess

def get_reference_parameters(only_required=True):
    ''' Возвращает список параметров '''
    if only_required:
        return ('directory', )
    else:
        return ('directory', 'extra_param', 'ignore_name', 'check_md5sum')

def config_find(directory, extra_param='', ignore_name='.*', check_md5sum=False):
    '''
       Конфигурация поиска файлов
       in: config_find(directory=<name-directory>, extra_param=<extra-param>, ignore_name=<ignore-name>, check_md5sum=<check_md5sum>)
           opts: str directory - имя деректории в которой искать файлы, обязательный параметр
           opts: str extra_param: - дополнительные параметры поиска см. man find, не обязательный параметр (значение по умолчанию '')
           opts: str ignore_name - имя файлов, которые необходимо исключить из поиска, не обязательный параметр (значение по умолчанию '.*')
           opts: bool check_md5sum - опция подсчета контрольной суммы по алгоритму md5 (значение по умолчанию False)
       out: (cmd, error_msg)
    '''
    try:
        ignore_name_cmd = '-not -name "{}"'.format(str(ignore_name)) if ignore_name else ''
        check_md5sum_cmd = 'md5=($(md5sum -b "$1")); echo -ne "$md5\n";' if check_md5sum else 'echo -ne "-\n";'
        cmd = '''find {0} {1} -type f {2} -printf "%p\t%h\t%f\t%u\t%g\t%s\t%TY-%Tm-%Td %TT\t" -exec bash -c '{3}' excec-sh {{}} ';'
              '''.format(directory, extra_param, ignore_name_cmd, check_md5sum_cmd)
        last_new_line = cmd.rfind('\n')
        cmd = cmd[:last_new_line]
        return cmd, ''
    except Exception as exc:
        exc_type, exc_obj, _ = sys.exc_info()
        return '', 'Error create find command:\n{}: {}'.format(exc_type.__name__, exc_obj)

def convert_std_bash(in_out, in_error):
    ''' Преобразование вывода '''
    out_list = in_out.decode('utf-8').split('\n')
    out = tuple([item for item in out_list if item != ''])
    error_str = in_error.decode('utf-8')
    error = 'Error find:\n{}'.format(error_str) if error_str else ''
    return out, error

def bash(cmd):
    ''' Выполнение bash-команды '''
    try:
        dialog = subprocess.Popen(['/bin/bash', '-c', cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, error = dialog.communicate()
        result_out, result_error = convert_std_bash(out, error)
        return result_out, result_error
    except Exception as exc:
        exc_type, exc_obj, _ = sys.exc_info()
        return (), 'Error bash:\n{}: {}'.format(exc_type.__name__, exc_obj)

def run(directory, extra_param='', ignore_name='.*', check_md5sum=False):
    '''
       Запуск поиска файлов
       in: run(directory=<name-directory>, extra_param=<extra-param>, ignore_name=<ignore-name>, check_md5sum=<check_md5sum>)
           opts: str directory - имя деректории в которой искать файлы, обязательный параметр
           opts: str extra_param: - дополнительные параметры поиска см. man find, не обязательный параметр (значение по умолчанию '')
           opts: str ignore_name - имя файлов, которые необходимо исключить из поиска, не обязательный параметр (значение по умолчанию '.*')
           opts: bool check_md5sum - опция подсчета контрольной суммы по алгоритму md5 (значение по умолчанию False)
       out: (result, error)
    '''
    config_find_cmd, config_find_err = config_find(directory, extra_param, ignore_name, check_md5sum)
    if not config_find_err:
        result, error = bash(config_find_cmd)
        return result, error
    else:
        return (), config_find_err

if __name__ == '__main__':
    print('Даннный файл представляет собой модуль для использования в python')
    parameters = globals()
    print(parameters['__doc__'])