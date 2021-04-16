#!/usr/bin/python3
'''
Сравнение файлов в директориях с использованием различных методов
'''

import sys

def main():
    pass

if __name__ == '__main__':
    try:
        import config
        main()
    except Exception as exc:
        exc_type, exc_obj, _ = sys.exc_info()
        print('Error config file:\n{}: {}'.format(exc_type.__name__, exc_obj))



