'''
Сбор информации о файлах
'''

import lib.find_file_bash

class Collection():
    def __init__(self):
        self.__config = {}
        self.__config_status = (False, 'No configuration check was performed')
        self.__reference_config = ('method', 'parameters')
        self.__reference_method = {
            'bash': 'lib.find_file_bash',
            'ssh': ''
        }
        self.__file_list = {}

    def clear_config(self):
        ''' Очистка конфигурации для сбора информации о файлах '''
        self.__config = {}
        return True

    def check_config(self):
        ''' Проверка файла конфигурации '''
        if type(self.__config) is not dict:
            self.__config_status = (False, 'Error: the configuration is not a dictionary')
            return False
        
        for item in self.__reference_config:
            if not item in self.__config.keys():
                self.__config[item] = ''
        
        if not self.__config['method'] in self.__reference_method.keys():
            self.__config_status = (False, 'Error: the method "{}" not found, \
use one of the {}'.format(self.__config['method'], ' | '.join(self.__reference_method.keys())))
            return False

        if type(self.__config['parameters']) is not dict:
            self.__config_status = (False, 'Error: the parameters configuration is not a dictionary')
            return False

        for pc_name in self.__config['parameters'].keys():
            reference_parameters = eval('{}.{}'.format(self.__reference_method[self.__config['method']], 'get_reference_parameters()'))
            for item in reference_parameters:
                if not item in self.__config['parameters'][pc_name].keys():
                    self.__config_status = (False, 'Error: the {} parameters "{}" not found'.format(pc_name, item))
                    return False
        
        self.__config_status = (True, 'Verification was successful')
        return True

    def add_pc_parameters(self, pc_name, **kwarg):
        ''' Добавление компьютера в параметров конфигурации '''
        self.__config['parameters'][pc_name] = kwarg
        return self.check_config()

    def delete_pc_parameters(self, pc_name):
        ''' Удаление компьютера из параметров конфигурации '''
        _ = self.__config['parameters'].pop(pc_name, None)
        return self.check_config()

    def set_config(self, data):
        '''
        Задать новое значение конфигурации:
        example-1 - пример для bash:
        {
            'method': 'bash',
            'parameters': {
                'pc1': {
                    'directory': '/tmp',
                    'extra_param': '',
                    'ignore_name': '.*',
                    'check_md5sum': False
                },
                'pc2': {
                    'directory': '/tmp',
                    'extra_param': '',
                    'ignore_name': '.*',
                    'check_md5sum': False
                }
            }
        }
        example-2 - пример для ssh:
        {
            'method': 'ssh',
            'parameters': {
                'pc1': {
                    'ip': '127.0.0.1',
                    'port': '22',
                    'username': 'user',
                    'password': '12345678',
                    'directory': '/tmp',
                    'extra_param': '-maxdepth 1',
                    'ignore_name': '.*',
                    'check_md5sum': True
                },
                'pc2': {
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
        example-3 - пример обновления толька части параметров:
        {
            'method': 'bash',
            'extra_param': ''
        }
        '''
        self.__config = data
        return self.check_config()

    def get_config(self):
        ''' Вернуть параметры '''
        return self.__config

    def get_config_status(self):
        ''' Вернуть состояние конфигурации '''
        return self.__config_status

    def get_file_list(self):
        ''' Вернуть список файлов и информации к ним '''
        return self.__file_list

    def run(self):
        ''' Сбор информации о файлах '''
        self.check_config()
        reference_parameters_all = eval('{}.{}'.format(self.__reference_method[self.__config['method']], 'get_reference_parameters(False)'))
        if self.__config_status[0]:
            for pc_name in self.__config['parameters'].keys():
                parameters = {}
                for item in self.__config['parameters'][pc_name].keys():
                    if item in reference_parameters_all:
                        parameters[item] = self.__config['parameters'][pc_name][item]
                cmd = '{}.{}'.format(self.__reference_method[self.__config['method']], 'run(**{})'.format(parameters))
                result, error = eval(cmd)
                self.__file_list[pc_name]['result'] = result
                self.__file_list[pc_name]['error'] = error

if __name__ == '__main__':
    print('Даннный файл представляет собой модуль для использования в python')
    parameters = globals()
    print(parameters['__doc__'])