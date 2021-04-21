'''
-------------------- Создание отчета по результатам поиска --------------------
ver.1.0
--------------------
IN: find_result = {
    'target_1': {
                'result': (
                    'path_file_1 \\t dir_file_1 \\t name_file_1 \\t user_f1 \\t group_f1 \\t size_f1 \\t date_modify_f1 \\t md5sum_f1',
                    'path_file_2 \\t dir_file_2 \\t name_file_2 \\t user_f2 \\t group_f2 \\t size_f2 \\t date_modify_f2 \\t md5sum_f2',
                    'path_file_3 \\t dir_file_3 \\t name_file_3 \\t user_f3 \\t group_f3 \\t size_f3 \\t date_modify_f3 \\t md5sum_f3',
                    'path_file_4 \\t dir_file_4 \\t name_file_4 \\t user_f4 \\t group_f4 \\t size_f4 \\t date_modify_f4 \\t md5sum_f4'
                    )
                'error': ''
                },
    'target_2': {
                'result': (
                    'path_file_1 \\t dir_file_1 \\t name_file_1 \\t user_f1 \\t group_f1 \\t size_f1 \\t date_modify_f1 \\t md5sum_f1',
                    'path_file_2 \\t dir_file_2 \\t name_file_2 \\t user_f2 \\t group_f2 \\t size_f2 \\t date_modify_f2 \\t md5sum_f2',
                    'path_file_3 \\t dir_file_3 \\t name_file_3 \\t user_f3 \\t group_f3 \\t size_f3 \\t date_modify_f3 \\t md5sum_f3',
                    'path_file_4 \\t dir_file_5 \\t name_file_4 \\t user_f4 \\t group_f4 \\t size_f4 \\t date_modify_f4 \\t md5sum_f4'
                    )
                'error': ''
                },
    'target_3': {
                'result': (
                    'path_file_1 \\t dir_file_1 \\t name_file_1 \\t user_f1 \\t group_f1 \\t size_f1 \\t date_modify_f1 \\t md5sum_f1',
                    'path_file_2 \\t dir_file_2 \\t name_file_2 \\t user_f2 \\t group_f2 \\t size_f2 \\t date_modify_f2 \\t md5sum_f2',
                    'path_file_3 \\t dir_file_3 \\t name_file_3 \\t user_f3 \\t group_f3 \\t size_f3 \\t date_modify_f3 \\t md5sum_f3',
                    'path_file_4 \\t dir_file_4 \\t name_file_4 \\t user_f4 \\t group_f4 \\t size_f4 \\t date_modify_f4 \\t md5sum_f4'
                    )
                'error': ''
                }
}
--------------------
OUT: target - None - all
    
    <object>.run('show_type': 'target', 'show_subtract': '', 'show_select': 'all'):
    <object>.get_report_dict()
    {
        'result': {
           'target_1': (
                ('dir_file_1', 'name_file_1', 'user_f1', 'group_f1', 'size_f1', 'date_modify_f1', 'md5sum_f1'),
                ('dir_file_2', 'name_file_2', 'user_f2', 'group_f2', 'size_f2', 'date_modify_f2', 'md5sum_f2'),
                ('dir_file_3', 'name_file_3', 'user_f3', 'group_f3', 'size_f3', 'date_modify_f3', 'md5sum_f3'),
                ('dir_file_4', 'name_file_4', 'user_f4', 'group_f4', 'size_f4', 'date_modify_f4', 'md5sum_f4')
                ),
           'target_2': (
                ('dir_file_1', 'name_file_1', 'user_f1', 'group_f1', 'size_f1', 'date_modify_f1', 'md5sum_f1'),
                ('dir_file_2', 'name_file_2', 'user_f2', 'group_f2', 'size_f2', 'date_modify_f2', 'md5sum_f2'),
                ('dir_file_3', 'name_file_3', 'user_f3', 'group_f3', 'size_f3', 'date_modify_f3', 'md5sum_f3'),
                ('dir_file_4', 'name_file_4', 'user_f4', 'group_f4', 'size_f4', 'date_modify_f4', 'md5sum_f4')
                ),
           'target_3': (
                ('dir_file_1', 'name_file_1', 'user_f1', 'group_f1', 'size_f1', 'date_modify_f1', 'md5sum_f1'),
                ('dir_file_2', 'name_file_2', 'user_f2', 'group_f2', 'size_f2', 'date_modify_f2', 'md5sum_f2'),
                ('dir_file_3', 'name_file_3', 'user_f3', 'group_f3', 'size_f3', 'date_modify_f3', 'md5sum_f3'),
                ('dir_file_4', 'name_file_4', 'user_f4', 'group_f4', 'size_f4', 'date_modify_f4', 'md5sum_f4')
                )
            },
        'error': {
           'target_1': 'error_txt',
           'target_2': 'error_txt',
           'target_3': 'error_txt'
            }
    }

OUT: target - None - match_name | match_md5sum
target_1: name_file_1 = name_file_2
          md5sum_file_1 = md5sum_file_2
target_2: name_file_2 = name_file_3
          md5sum_file_2 = md5sum_file_3
target_3: name_file_1 = name_file_2, name_file_3 =  name_file_4
          md5sum_file_1 = md5sum_file_2, md5sum_file_3 = md5sum_file_4
    
    <object>.run('show_type': 'target', 'show_subtract': '', 'show_select': 'match_name'):
    <object>.get_report_dict()
    {
        'result': {
           'target_1': (
                ('dir_file_1', 'name_file_1', 'user_f1', 'group_f1', 'size_f1', 'date_modify_f1', 'md5sum_f1'),
                ('dir_file_2', 'name_file_2', 'user_f2', 'group_f2', 'size_f2', 'date_modify_f2', 'md5sum_f2')
                ),
           'target_2': (
                ('dir_file_2', 'name_file_2', 'user_f2', 'group_f2', 'size_f2', 'date_modify_f2', 'md5sum_f2'),
                ('dir_file_3', 'name_file_3', 'user_f3', 'group_f3', 'size_f3', 'date_modify_f3', 'md5sum_f3')
                ),
           'target_3': (
                ('dir_file_1', 'name_file_1', 'user_f1', 'group_f1', 'size_f1', 'date_modify_f1', 'md5sum_f1'),
                ('dir_file_2', 'name_file_2', 'user_f2', 'group_f2', 'size_f2', 'date_modify_f2', 'md5sum_f2'),
                ('dir_file_3', 'name_file_3', 'user_f3', 'group_f3', 'size_f3', 'date_modify_f3', 'md5sum_f3'),
                ('dir_file_4', 'name_file_4', 'user_f4', 'group_f4', 'size_f4', 'date_modify_f4', 'md5sum_f4')
                )
            },
        'error': {
           'target_1': 'error_txt',
           'target_2': 'error_txt',
           'target_3': 'error_txt'
            }
    }

OUT: target - None - diff_name | diff_md5sum
target_1: name_file_1 = name_file_2
          md5sum_file_1 = md5sum_file_2
target_2: name_file_2 = name_file_3
          md5sum_file_2 = md5sum_file_3
target_3: name_file_1 = name_file_2, name_file_3 =  name_file_4
          md5sum_file_1 = md5sum_file_2, md5sum_file_3 = md5sum_file_4
    
    <object>.run('show_type': 'target', 'show_subtract': '', 'show_select': 'diff_name'):
    <object>.get_report_dict()
    {
        'result': {
           'target_1': (
                ('dir_file_3', 'name_file_3', 'user_f3', 'group_f3', 'size_f3', 'date_modify_f3', 'md5sum_f3'),
                ('dir_file_4', 'name_file_4', 'user_f4', 'group_f4', 'size_f4', 'date_modify_f4', 'md5sum_f4')
                ),
           'target_2': (
                ('dir_file_1', 'name_file_1', 'user_f1', 'group_f1', 'size_f1', 'date_modify_f1', 'md5sum_f1'),
                ('dir_file_4', 'name_file_4', 'user_f4', 'group_f4', 'size_f4', 'date_modify_f4', 'md5sum_f4')
                ),
           'target_3': ()
            },
        'error': {
           'target_1': 'error_txt',
           'target_2': 'error_txt',
           'target_3': 'error_txt'
            }
    }
--------------------
OUT: path | keep_path | md5sum - None - all
    
    <object>.run('show_type': 'path', 'show_subtract': '', 'show_select': 'all'):
    <object>.get_report_dict()
    {
        'result': {
           'path_file_1' | 'keep_path_1' | 'md5sum_1': (
                ('target_1', 'dir_file_1', 'name_file_1', 'user_f1', 'group_f1', 'size_f1', 'date_modify_f1', 'md5sum_f1'),
                ('target_2', 'dir_file_1', 'name_file_1', 'user_f1', 'group_f1', 'size_f1', 'date_modify_f1', 'md5sum_f1'),
                ('target_3', 'dir_file_1', 'name_file_1', 'user_f1', 'group_f1', 'size_f1', 'date_modify_f1', 'md5sum_f1')
                ),
           'path_file_2'| 'keep_path_2' | 'md5sum_2': (
                ('target_1', 'dir_file_2', 'name_file_2', 'user_f2', 'group_f2', 'size_f2', 'date_modify_f2', 'md5sum_f2'),
                ('target_2', 'dir_file_2', 'name_file_2', 'user_f2', 'group_f2', 'size_f2', 'date_modify_f2', 'md5sum_f2'),
                ('target_3', 'dir_file_2', 'name_file_2', 'user_f2', 'group_f2', 'size_f2', 'date_modify_f2', 'md5sum_f2')
                },
           'path_file_3'| 'keep_path_3' | 'md5sum_3': (
                ('target_1', 'dir_file_3', 'name_file_3', 'user_f3', 'group_f3', 'size_f3', 'date_modify_f3', 'md5sum_f3'),
                ('target_2', 'dir_file_3', 'name_file_3', 'user_f3', 'group_f3', 'size_f3', 'date_modify_f3', 'md5sum_f3'),
                ('target_3', 'dir_file_3', 'name_file_3', 'user_f3', 'group_f3', 'size_f3', 'date_modify_f3', 'md5sum_f3')
                },
           'path_file_4'| 'keep_path_4' | 'md5sum_4': (
                ('target_1', 'dir_file_4', 'name_file_4', 'user_f4', 'group_f4', 'size_f4', 'date_modify_f4', 'md5sum_f4'),
                ('target_2', 'dir_file_4', 'name_file_4', 'user_f4', 'group_f4', 'size_f4', 'date_modify_f4', 'md5sum_f4'),
                ('target_3', 'dir_file_4', 'name_file_4', 'user_f4', 'group_f4', 'size_f4', 'date_modify_f4', 'md5sum_f4')
                ),
            },
        'error': {
           'target_1': 'error_txt',
           'target_2': 'error_txt',
           'target_3': 'error_txt'
            }
    }

OUT: path | keep_path | md5sum - None - match_size | match_md5sum
path_file_1:
    target_1-size_f1 = target_2-size_f1
    target_1-md5sum_f1 = target_2-md5sum_f1
path_file_2:
    target_2-size_f2 = target_3-size_f2
    target_2-md5sum_f2 = target_3-md5sum_f2
path_file_3:
    target_1-size_f3 = target_3-size_f3
    target_1-md5sum_f3 = target_3-md5sum_f3
path_file_4:
    target_1-size_f4 = target_2-size_f4 = target_3-size_f4
    target_1-md5sum_f4 = target_2-md5sum_f4 = target_3-md5sum_f4
    
    <object>.run('show_type': 'path', 'show_subtract': '', 'show_select': 'match_name'):
    <object>.get_report_dict()
    {
        'result': {
           'path_file_1' | 'keep_path_1' | 'md5sum_1': (
                ('target_1', 'dir_file_1', 'name_file_1', 'user_f1', 'group_f1', 'size_f1', 'date_modify_f1', 'md5sum_f1'),
                ('target_2', 'dir_file_1', 'name_file_1', 'user_f1', 'group_f1', 'size_f1', 'date_modify_f1', 'md5sum_f1')
                ),
           'path_file_2'| 'keep_path_2' | 'md5sum_2': (
                ('target_2', 'dir_file_2', 'name_file_2', 'user_f2', 'group_f2', 'size_f2', 'date_modify_f2', 'md5sum_f2'),
                ('target_3', 'dir_file_2', 'name_file_2', 'user_f2', 'group_f2', 'size_f2', 'date_modify_f2', 'md5sum_f2')
                },
           'path_file_3'| 'keep_path_3' | 'md5sum_3': (
                ('target_1', 'dir_file_3', 'name_file_3', 'user_f3', 'group_f3', 'size_f3', 'date_modify_f3', 'md5sum_f3'),
                ('target_3', 'dir_file_3', 'name_file_3', 'user_f3', 'group_f3', 'size_f3', 'date_modify_f3', 'md5sum_f3')
                },
           'path_file_4'| 'keep_path_4' | 'md5sum_4': (
                ('target_1', 'dir_file_4', 'name_file_4', 'user_f4', 'group_f4', 'size_f4', 'date_modify_f4', 'md5sum_f4'),
                ('target_2', 'dir_file_4', 'name_file_4', 'user_f4', 'group_f4', 'size_f4', 'date_modify_f4', 'md5sum_f4'),
                ('target_3', 'dir_file_4', 'name_file_4', 'user_f4', 'group_f4', 'size_f4', 'date_modify_f4', 'md5sum_f4')
                },
            },
        'error': {
           'target_1': 'error_txt',
           'target_2': 'error_txt',
           'target_3': 'error_txt'
            }
    }

OUT: path | keep_path | md5sum - None - diff_size | diff_md5sum
path_file_1:
    target_1-size_f1 = target_2-size_f1
    target_1-md5sum_f1 = target_2-md5sum_f1
path_file_2:
    target_2-size_f2 = target_3-size_f2
    target_2-md5sum_f2 = target_3-md5sum_f2
path_file_3:
    target_1-size_f3 = target_3-size_f3
    target_1-md5sum_f3 = target_3-md5sum_f3
path_file_4:
    target_1-size_f4 = target_2-size_f4 = target_3-size_f4
    target_1-md5sum_f4 = target_2-md5sum_f4 = target_3-md5sum_f4
    
    <object>.run('show_type': 'path', 'show_subtract': '', 'show_select': 'diff_size'):
    <object>.get_report_dict()
    {
        'result': {
           'path_file_1' | 'keep_path_1' | 'md5sum_1': (
                ('target_3', 'dir_file_1', 'name_file_1', 'user_f1', 'group_f1', 'size_f1', 'date_modify_f1', 'md5sum_f1')
                ),
           'path_file_2'| 'keep_path_2' | 'md5sum_2': (
                ('target_1', 'dir_file_2', 'name_file_2', 'user_f2', 'group_f2', 'size_f2', 'date_modify_f2', 'md5sum_f2')
                },
           'path_file_3'| 'keep_path_3' | 'md5sum_3': (
                ('target_2', 'dir_file_3', 'name_file_3', 'user_f3', 'group_f3', 'size_f3', 'date_modify_f3', 'md5sum_f3')
                },
           'path_file_4'| 'keep_path_4' | 'md5sum_4': (),
            },
        'error': {
           'target_1': 'error_txt',
           'target_2': 'error_txt',
           'target_3': 'error_txt'
            }
    }


'''

def get_reference_type():
    ''' Вернуть список допустимых значений для генерации отчета '''
    return ('target', 'path', 'keep_path', 'md5sum')

def get_reference_select():
    ''' Вернуть список выборок из отчета '''
    return ('all', 'match_name', 'diff_name', 'match_md5sum', 'diff_md5sum')

class Create():
    def __init__():
        self.__find_result = {}
        self.__report_status = (False, 'The report was not generated')
        self.__report_dict = {}
        self.__report_txt = ''

    def set_find_result(self, data):
        ''' Задать найденные файлы '''
        if type(data) is dict:
            self.__find_result = data
            return True
        else:
            return False

    def get_find_result(self):
        ''' Вернуть найденные файлы '''
        return self.__find_result

    def get_report_status(self):
        ''' Вернуть статус создания отчета '''
        return self.__report_status

    def get_report_dict(self):
        ''' Вернуть отчет в виде словаря '''
        return self.__report_dict

    def get_report_txt(self):
        ''' Вернуть отчет в текстовом виде '''
        return self.__report_txt
    
    def get_

    def create_report_target(self, show_select='all'):
        '''
           Генерация отчета по целям
        '''




    def create_all(self):
        '''
           Генерация отчета для всех данных
        '''


        pc_name_list = self.__line_stdout.keys()
        # Проходим по всем компьютерам с которых собрали информацию о файлах
        for pc_name in pc_name_list:
            # Структурируем информацию
            for item in self.__line_stdout[pc_name].split('\n')[:-1]:
                data = tuple(item.split('\t'))
                try:
                    file_name = data[0]
                    if file_name:
                        # Если в отчете отсутсвует ключ с именм файла, то мы его создаем
                        if file_name not in self.__file_list['out'].keys():
                            self.__file_list['out'][file_name] = {}
                        # Если для компьютеров не задано значения параметор файла, то мы зполняем его пустым значением
                        for pc_name_check in pc_name_list:
                            if pc_name_check not in self.__file_list['out'][file_name].keys():
                                self.__file_list['out'][file_name][pc_name_check] = tuple(['-' for x in range(len([data]) - 1)])
                        # Обновляем значения параметров для заданного файла расположенного на конкретном компьютере
                        self.__file_list['out'][file_name][pc_name] = data[1:]
                except Exception as exc:
                    self.__file_list['error']['parsing'] += 'pc: {}, data: {}, msg_error: {}\n'.format(pc_name, data, exc)
            if pc_name in self.__file_list['error'].keys():
                self.__file_list['error'][pc_name] = self.__line_stderr[pc_name]


    def run(self, show_type='target', 'show_subtract': '', show_select='all'):
        ''' Генерация отчета '''
        pass


