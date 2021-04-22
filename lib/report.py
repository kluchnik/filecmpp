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
        'target_1': {
           'result': (
                ('target_1', 'dir_file_1', 'name_file_1', 'user_f1', 'group_f1', 'size_f1', 'date_modify_f1', 'md5sum_f1'),
                ('target_1', 'dir_file_2', 'name_file_2', 'user_f2', 'group_f2', 'size_f2', 'date_modify_f2', 'md5sum_f2'),
                ('target_1', 'dir_file_3', 'name_file_3', 'user_f3', 'group_f3', 'size_f3', 'date_modify_f3', 'md5sum_f3'),
                ('target_1', 'dir_file_4', 'name_file_4', 'user_f4', 'group_f4', 'size_f4', 'date_modify_f4', 'md5sum_f4')
                ),
           'error': ''
           },
        'target_2': {
           'result': (
                ('target_2', 'dir_file_1', 'name_file_1', 'user_f1', 'group_f1', 'size_f1', 'date_modify_f1', 'md5sum_f1'),
                ('target_2', 'dir_file_2', 'name_file_2', 'user_f2', 'group_f2', 'size_f2', 'date_modify_f2', 'md5sum_f2'),
                ('target_2', 'dir_file_3', 'name_file_3', 'user_f3', 'group_f3', 'size_f3', 'date_modify_f3', 'md5sum_f3'),
                ('target_2', 'dir_file_4', 'name_file_4', 'user_f4', 'group_f4', 'size_f4', 'date_modify_f4', 'md5sum_f4')
                ),
           'error': ''
           },
        'target_3': {
           'result': (
                ('target_3', 'dir_file_1', 'name_file_1', 'user_f1', 'group_f1', 'size_f1', 'date_modify_f1', 'md5sum_f1'),
                ('target_3', 'dir_file_2', 'name_file_2', 'user_f2', 'group_f2', 'size_f2', 'date_modify_f2', 'md5sum_f2'),
                ('target_3', 'dir_file_3', 'name_file_3', 'user_f3', 'group_f3', 'size_f3', 'date_modify_f3', 'md5sum_f3'),
                ('target_3', 'dir_file_4', 'name_file_4', 'user_f4', 'group_f4', 'size_f4', 'date_modify_f4', 'md5sum_f4')
                ),
           'error': ''
           }
    }

OUT: target - None - match_name | match_md5sum | match_name_size
target_1: name_file_1 = name_file_2
          md5sum_file_1 = md5sum_file_2
          size_file_1 = size_file_2
target_2: name_file_2 = name_file_3
          md5sum_file_2 = md5sum_file_3
          size_file_2 = size_file_3
target_3: name_file_1 = name_file_2, name_file_3 =  name_file_4
          md5sum_file_1 = md5sum_file_2, md5sum_file_3 = md5sum_file_4
          size_file_1 = size_file_2, size_file_3 = size_file_4
    
    <object>.run('show_type': 'target', 'show_subtract': '', 'show_select': 'match_name'):
    <object>.get_report_dict()
    {
        'target_1': {
           'result': (
                ('target_1', 'dir_file_1', 'name_file_1', 'user_f1', 'group_f1', 'size_f1', 'date_modify_f1', 'md5sum_f1'),
                ('target_1', 'dir_file_2', 'name_file_2', 'user_f2', 'group_f2', 'size_f2', 'date_modify_f2', 'md5sum_f2')
                ),
           'error': ''
           },
        'target_2': {
           'result': (
                ('target_2', 'dir_file_2', 'name_file_2', 'user_f2', 'group_f2', 'size_f2', 'date_modify_f2', 'md5sum_f2'),
                ('target_2', 'dir_file_3', 'name_file_3', 'user_f3', 'group_f3', 'size_f3', 'date_modify_f3', 'md5sum_f3')
                ),
           'error': ''
           },
        'target_3': {
           'result': (
                ('target_3', 'dir_file_1', 'name_file_1', 'user_f1', 'group_f1', 'size_f1', 'date_modify_f1', 'md5sum_f1'),
                ('target_3', 'dir_file_2', 'name_file_2', 'user_f2', 'group_f2', 'size_f2', 'date_modify_f2', 'md5sum_f2'),
                ('target_3', 'dir_file_3', 'name_file_3', 'user_f3', 'group_f3', 'size_f3', 'date_modify_f3', 'md5sum_f3'),
                ('target_3', 'dir_file_4', 'name_file_4', 'user_f4', 'group_f4', 'size_f4', 'date_modify_f4', 'md5sum_f4')
                ),
           'error': ''
           }
    }

OUT: target - None - diff_name | diff_md5sum | match_name_size
target_1: name_file_1 = name_file_2
          md5sum_file_1 = md5sum_file_2
          size_file_1 = size_file_2
target_2: name_file_2 = name_file_3
          md5sum_file_2 = md5sum_file_3
          size_file_2 = size_file_3
target_3: name_file_1 = name_file_2, name_file_3 =  name_file_4
          md5sum_file_1 = md5sum_file_2, md5sum_file_3 = md5sum_file_4
          size_file_1 = size_file_2, size_file_3 = size_file_4
    
    <object>.run('show_type': 'target', 'show_subtract': '', 'show_select': 'diff_name'):
    <object>.get_report_dict()
    {
        'target_1': {
           'result': (
                ('target_1', 'dir_file_3', 'name_file_3', 'user_f3', 'group_f3', 'size_f3', 'date_modify_f3', 'md5sum_f3'),
                ('target_1', 'dir_file_4', 'name_file_4', 'user_f4', 'group_f4', 'size_f4', 'date_modify_f4', 'md5sum_f4')
                ),
           'error': ''
           },
        'target_2': {
           'result': (
                ('target_2', 'dir_file_1', 'name_file_1', 'user_f1', 'group_f1', 'size_f1', 'date_modify_f1', 'md5sum_f1'),
                ('target_2', 'dir_file_4', 'name_file_4', 'user_f4', 'group_f4', 'size_f4', 'date_modify_f4', 'md5sum_f4')
                ),
           'error': ''
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
                ),
           'path_file_3'| 'keep_path_3' | 'md5sum_3': (
                ('target_1', 'dir_file_3', 'name_file_3', 'user_f3', 'group_f3', 'size_f3', 'date_modify_f3', 'md5sum_f3'),
                ('target_2', 'dir_file_3', 'name_file_3', 'user_f3', 'group_f3', 'size_f3', 'date_modify_f3', 'md5sum_f3'),
                ('target_3', 'dir_file_3', 'name_file_3', 'user_f3', 'group_f3', 'size_f3', 'date_modify_f3', 'md5sum_f3')
                ),
           'path_file_4'| 'keep_path_4' | 'md5sum_4': (
                ('target_1', 'dir_file_4', 'name_file_4', 'user_f4', 'group_f4', 'size_f4', 'date_modify_f4', 'md5sum_f4'),
                ('target_2', 'dir_file_4', 'name_file_4', 'user_f4', 'group_f4', 'size_f4', 'date_modify_f4', 'md5sum_f4'),
                ('target_3', 'dir_file_4', 'name_file_4', 'user_f4', 'group_f4', 'size_f4', 'date_modify_f4', 'md5sum_f4')
                )
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
                ),
           'path_file_3'| 'keep_path_3' | 'md5sum_3': (
                ('target_1', 'dir_file_3', 'name_file_3', 'user_f3', 'group_f3', 'size_f3', 'date_modify_f3', 'md5sum_f3'),
                ('target_3', 'dir_file_3', 'name_file_3', 'user_f3', 'group_f3', 'size_f3', 'date_modify_f3', 'md5sum_f3')
                ),
           'path_file_4'| 'keep_path_4' | 'md5sum_4': (
                ('target_1', 'dir_file_4', 'name_file_4', 'user_f4', 'group_f4', 'size_f4', 'date_modify_f4', 'md5sum_f4'),
                ('target_2', 'dir_file_4', 'name_file_4', 'user_f4', 'group_f4', 'size_f4', 'date_modify_f4', 'md5sum_f4'),
                ('target_3', 'dir_file_4', 'name_file_4', 'user_f4', 'group_f4', 'size_f4', 'date_modify_f4', 'md5sum_f4')
                )
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
                ),
           'path_file_3'| 'keep_path_3' | 'md5sum_3': (
                ('target_2', 'dir_file_3', 'name_file_3', 'user_f3', 'group_f3', 'size_f3', 'date_modify_f3', 'md5sum_f3')
                )
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
    return ('all', 'match_name', 'match_size', 'match_md5sum', 'match_name_size',
            'diff_name', 'diff_size', 'diff_md5sum', 'diff_name_size')

class Create():
    def __init__():
        self.__find_result = {}
        self.__data_structure = ('target', 'path', 'dir', 'name', 'user', 'group', 'size', 'date_modify', 'md5sum')
        self.__data_map = {
            'match_name': (3,), 'match_size': (6,), 'match_md5sum': (8,), 'match_name_size': (3, 6),
            'diff_name': (3,), 'diff_size': (6,), 'diff_md5sum': (8,), 'diff_name_size': (3, 6)
            }
        self.__data_dimension = len(self.__data_structure)
        self.__report_status = (False, 'The report was not generated')
        self.__report_dict = {}
        self.__report_txt = ''
    

    def check_find_result(self):
        ''' Проверить входные данные для отчета '''
        if type(self.__find_result) is not dict:
            self.__report_status = (False, 'Error check: find_result is not dict')
            self.__find_result = {}
            return False
        for target in self.__find_result.keys():
            if not 'result' in self.__find_result[target]:
                self.__report_status = (False, 'Error check: find_result is target "{}" missing "result"'.format(target))
                self.__find_result[target]['result'] = ()
                return False
            if not 'error' in self.__find_result[target]:
                self.__report_status = (False, 'Error check: find_result is target "{}" missing "error"'.format(target))
                self.__find_result[target]['error'] = ''
                return False
        return True

    def set_find_result(self, data):
        ''' Задать найденные файлы '''
        self.__find_result = data
        return self.check_find_result()

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
    
    def get_file_tuple(self, file_info_str):
        ''' Возвращает кортеж с данными о файле '''
        try:
            file_info_str = str(file_info_str)
            file_info_tuple = tuple(file_info_str.split('\t'))
            delta =  tuple(['-' for x in range(self.__data_dimension - len(file_info_tuple))])
            file_info_tuple = file_info_tuple + delta
        except:
            file_info_tuple = tuple(['-' for x in range(self.__data_dimension)])
        return file_info_tuple

    def get_data_select(self, select_type='', data):
        ''' Возвращает список параметров указанных в select_type, согласно self.__data_map '''
        data_select = ()
        len_data = len(data)
        
        if match_type in self.__data_map.keys():
            match_index = self.__data_map[select_type]
        else:
        	match_index = (1,)
        
        for item in range(len_data):
            item_select = ()
            for index in match_index:
                item_select += data[item][index]
            data_select += (item_select, )
        
        return data_select

    def get_match(self, match_type='', data):
        ''' Возвращает совпадающие данные из списка '''
        if match_type in self.__data_map.keys():
            data_select = self.get_data_select(select_type=match_type, data):
            len_data = len(data)
            data_math = ()

            for i_index in range(len_data - 1):
                for j_index in range(i_index, len_data):
                    if data_select[i_index] == data_select[j_index]:
                        data_math += (data[i_index], )
                        data_math += (data[j_index], )

            data_math = tuple(set(data_math))
            return data_math
        else:
            return data

    def get_diff(self, diff_type='', data):
        ''' Возвращает отличные данные из списка '''
        if match_type in self.__data_map.keys():
            data_match = self.get_match(self, match_type=diff_type, data):
            data_diff = tuple(set(data) - set(data_match))
            return data_diff
        else:
            return data

    def create_report_target(self, show_select='all'):
        '''
           Генерация отчета по целям
        '''
        _ = self.check_find_result()
        report_dict_tmp = {}
        target_list = self.__find_result.keys()
        for target in target_list:
            report_dict_tmp[target] = {}
            report_dict_tmp[target]['result'] = ()
            for item in self.__find_result[target]['result']:
                report_dict_tmp[target]['result'] += (self.get_file_tuple('{}\t{}'.format(target, item)), )
            report_dict_tmp[target]['error'] = ''
        
        report_dict = {}
        for target in target_list:
        	report_dict[target] = {}
            if 'match' in show_select:
                report_dict[target]['result'] = self.get_match(match_type=show_select, report_dict_tmp[target]['result'])
            elif 'diff' in show_select::
                report_dict[target]['result'] = self.get_diff(match_type=show_select, report_dict_tmp[target]['result'])
            else:
                report_dict[target]['result'] = report_dict_tmp[target]['result']
            report_dict[target]['error'] = report_dict_tmp[target]['error']
        
        return report_dict

    def create_report_path(self, show_select='all'):
        '''
           Генерация отчета по целям
        '''
        data_target = self.create_report_target(show_select='all'):
        report_dict_tmp = {'result': {}, 'error': {}}
        target_list = data_target.keys()
        # Проходим по всем целям
        for target in target_list:
            # Структурируем информацию по path
            for item in target_list[target]['result']:
                path = target_list[target]['result'][1]
                # Если в отчете отсутсвует ключ с путем и именем файла (path), то мы его создаем
                if path not in report_dict_tmp['result'].keys():
                    report_dict_tmp['result'][path] = {}
                # Если для цели не заданы значения параметров файла, то мы зполняем его пустыми значениями
                for target_check in target_list:
                    if target_check not in report_dict_tmp['result'][path].keys():
                        report_dict_tmp['result'][path][target_check] = self.get_file_tuple(None)





                            
                        
                        
                            
                                s
                        # Обновляем значения параметров для заданного файла расположенного на конкретном компьютере
                        self.__file_list['out'][file_name][pc_name] = data[1:]
                except Exception as exc:
                    self.__file_list['error']['parsing'] += 'pc: {}, data: {}, msg_error: {}\n'.format(pc_name, data, exc)
            if pc_name in self.__file_list['error'].keys():
                self.__file_list['error'][pc_name] = self.__line_stderr[pc_name]



            report_dict_tmp[target] = {}
            report_dict_tmp[target]['result'] = ()
            for item in self.__find_result[target]['result']:
                report_dict_tmp[target]['result'] += (self.get_file_tuple((target,) + item), )
            report_dict_tmp[target]['error'] = ''
        




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


