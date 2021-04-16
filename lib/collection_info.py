'''
Сбор информации о файлах
'''

class Collection():
    def __init__(self):
        self.__config = {}
        self.__status_config = (False, 'No configuration check was performed')
        self.__status_find = ()
        self.__reference_config = ('method', 'extra_param', 'ignore_name', 'check_md5sum', 'parameters')
        self.__reference_method = {
            'bash': ('directory', ),
            'ssh': ('ip', 'port', 'username', 'password', 'directory')
        }
        #self.__
        #self.__line_stdout = {}
        #self.__line_stderr = {}
        #self.__extra_param = ''
        #self.__ignore_name = '.*'
        #self.__check_md5sum = False
        #self.__file_list = {'out': {}, 'error': {}}

    def clear_config(self):
        ''' Очистка конфигурации для сбора информации о файлах '''
        self.__config = {}
        return True

    def check_config(self):
        ''' Проверка файла конфигурации '''
        if self.__config is not dict:
            self.__status_config = (False, 'Error: the configuration is not a dictionary')
            return False
        
        for item in self.__reference_config:
            if item is not self.__config.keys():
                self.__config[item] = ''
        
        if self.__config['method'] is not self.__reference_method.keys():
            self.__status_config = (False, 'Error: the method "{}" not found, \
            	use one of the {}'.format(self.__config['method'], ' | '.join(self.__reference_method.keys())))
            return False
        
        if self.__config['parameters'] is not dict:
            self.__status_config = (False, 'Error: the parameters configuration is not a dictionary')
            return False

        for pc_name in self.__config['parameters'].keys():
            for item in self.__config['parameters'][pc_name].keys():
                if self.__config['parameters'][pc_name][item] is not self.__reference_method[self.__config['method']]:
                    self.__status_config = (False, 'Error: the {} parameters "{}" not found'.format(pc_name, item))
                    return False
        
        self.__status_config = (True, 'Verification was successful')
        return True

    def add_pc_parameters(self, name_pc, **kwarg):
        ''' Добавление компьютера в параметров конфигурации '''
        self.__config['parameters'][name_pc] = kwarg
        return self.check_config()

    def delete_pc_parameters(self, name_pc):
        ''' Удаление компьютера из параметров конфигурации '''
        _ = self.__config['parameters'].pop(name_pc, None)
        return self.check_config()

    def set_parameters(self, data):
        '''
        Задать новое значение конфигурации:
        example-1:
        {
            'method': 'bash',
            'extra_param': '',
            'ignore_name': '.*',
            'check_md5sum': False,
            'parameters': {
                'pc1': {'directory': '/tmp'},
                'pc2': {'directory': '/tmp'}
            }
        }
        example-2:
        {
            'method': 'ssh',
            'extra_param': '-maxdepth 1',
            'ignore_name': '.*',
            'check_md5sum': True,
            'parameters': {
                'pc1': {
                    'ip': '127.0.0.1',
                    'port': '22',
                    'username': 'user',
                    'password': '12345678',
                    'directory': '/tmp'
                },
                'pc2': {
                    'ip': '127.0.0.1',
                    'port': '22',
                    'username': 'user',
                    'password': '12345678',
                    'directory': '/tmp'
                }
        }
        '''
        self.__parameters = data
        return self.check_config()

    def get_parameters(self):
        ''' Вернуть параметры '''
        return self.__parameters

    def run_file_status(self):
        ''' Сбор информации о файлах '''
        for pc_name in self.__parameters.keys():
            if self.connect(pc_name):
                directory = self.__parameters[pc_name]['directory']
                self.command(pc_name, self.config_find(directory))
                self.disconnect()



if __name__ == '__main__':
    print('Даннный файл представляет собой модуль для использования в python')
    parameters = globals()
    print(parameters['__doc__'])