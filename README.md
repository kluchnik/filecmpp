# filecmpp
File comparison plus (local and remote)

Архитектура приложения:  
.  
|- filecmpp.py (Запуск приложения)  
|- lib  
|&nbsp;&nbsp;&nbsp;&nbsp;|- \_\_init\_\_.py  
|&nbsp;&nbsp;&nbsp;&nbsp;|- collection_info.py (Сбор информации о файлах)  
|&nbsp;&nbsp;&nbsp;&nbsp;|- find_file_bash.py (Поиск файлов через bash)  
|&nbsp;&nbsp;&nbsp;&nbsp;|- find_file_ssh.py (Поиск файлов через ssh)  
|&nbsp;&nbsp;&nbsp;&nbsp;|- cmp_path.py (Сравнение файлов по пути)  
|&nbsp;&nbsp;&nbsp;&nbsp;|- cmp_name.py (Сравнение файлов по имени)  
|&nbsp;&nbsp;&nbsp;&nbsp;|- cmp_md5.py (Сравнение файлов по md5)  
|- test (Тестовый сценарий)  
|- ?  
