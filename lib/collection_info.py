'''
-------------------- Сбор информации о файлах --------------------
ver.1.1
--------------------
Пример использования:
--------------------
import collection_info

collection = collection_info.Collection()
config = 
collection.set_config(config)

'''

import lib.check_config

class Collection():
    def __init__(self):
        self.__config = {}
        self.__config_status = (False, 'No configuration check was performed')
        self.__find_module = None
        self.__find_config = {}
        self.__find_status = (False, 'No run find')
        self.__find_result = {}

    def clear_config(self):
        ''' Очистка конфигурации для сбора информации о файлах '''
        self.__config = {}
        return True

    def check_config(self):
        ''' Прооверить конфигурацию '''
        try:
            result = lib.check_config.run(self.__config)
            self.__config_status = result[:2]
            self.__find_module = result[2]
            self.__find_config = result[3]
            return self.__config_status[0]
        except Exception as exc:
            self.__config_status = (False, 'Error: check config {}'.format(exc))
            return self.__config_status[0]

    def set_config(self, data):
        ''' Задать новое значение конфигурации '''
        self.__config = data
        return self.check_config()

    def get_config(self):
        ''' Вернуть значения конфигурации '''
        return self.__config

    def get_config_status(self):
        ''' Вернуть состояние конфигурации '''
        return self.__config_status

    def get_find_module(self):
        ''' Вернуть поисковый модуль '''
        return self.__find_module

    def get_find_config(self):
        ''' Вернуть конфигурацию для поиска '''
        return self.__find_config

    def get_find_status(self):
        ''' Вернуть состояние поиска '''
        return self.__find_status

    def get_find_result(self):
        ''' Вернуть список файлов и информации к ним по резултатам поиска '''
        return self.__find_result

    def run(self):
        ''' Сбор информации о файлах '''
        try:
            exec_cmd = 'import {}'.format(self.__find_module)
        except:
            self.__find_status = (False, 'Error: import module "{}"'.format(self.__find_module))
            return self.__find_status

        if not 'run' in eval('dir({})'.format(self.__find_module)):
            self.__find_status = (False, 'Error: method "run" not found in the module {}'.format(self.__find_module))
            return self.__find_status

        if self.check_config():
            for target in self.__find_config.keys():
                self.__find_result[target] = {}
                exec_cmd = '{}.run(**{})'.format(self.__find_module, self.__find_config[target])
                try:
                    result, error = eval(exec_cmd)
                    self.__find_result[target]['result'] = result
                    self.__find_result[target]['error'] = error
                except:
                    self.__find_result[target]['result'] = ''
                    self.__find_result[target]['error'] = 'Error: in the execution of the command\n{}'.format(exec_cmd)
        
        self.__find_status = (True, 'Find was successful')
        return True

if __name__ == '__main__':
    print('Даннный файл представляет собой модуль для использования в python')
    parameters = globals()
    print(parameters['__doc__'])