'''
-------------------- Модуль для поиска файлов через оболочку bash --------------------
ver.1.1
Пример использования:
--------------------
import comp_file_ssh

comp_file_ssh_ = comp_file_ssh.Comparison()
comp_file_ssh_.get_parameters()
comp_file_ssh_.delete_pc_parameters('pc2')
comp_file_ssh_.get_parameters()
comp_file_ssh_.clear_parameters()
comp_file_ssh_.get_parameters()

parameters_pc1 = {'ip': '192.168.1.11', 'port': '22', 'username': 'root', 'password': '12345678', 'directory': '/tmp'}
parameters_pc2 = {'ip': '192.168.1.12', 'port': '22', 'username': 'root', 'password': '12345678', 'directory': '/tmp'}
parameters_pc1 = {'ip': '127.0.0.1', 'port': '22', 'username': 'user', 'password': '12345678', 'directory': '/tmp/test1'}
parameters_pc2 = {'ip': '127.0.0.1', 'port': '22', 'username': 'user', 'password': '12345678', 'directory': '/tmp/test2'}
parameters = {'pc1': parameters_pc1, 'pc2': parameters_pc2}
comp_file_ssh_.set_parameters(**parameters)
comp_file_ssh_.get_parameters()

comp_file_ssh_.get_report()

--------------------
'''

import sys
import subprocess

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
       out: cmd_find | None
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