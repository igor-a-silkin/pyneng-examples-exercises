# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт: Скрипт не должен выводить на стандартрый поток вывода команды,
в которых содержатся слова из списка ignore.

При этом скрипт также не должен выводить строки, которые начинаются на !.

Проверить работу скрипта на конфигурационном файле config_sw1.txt.
Имя файла передается как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

from sys import argv

if len(argv) <= 1:
    print('File name is empty!')
else:
    try:
        file = []
        with open(argv[1],'r') as f:
            file = f.readlines()

        ignore = ['duplex', 'alias', 'Current configuration']

        for line in file:
            if not line.startswith('!'):
                is_ignore = False
                for item in ignore:
                     if line.count(item) > 0:
                        is_ignore = True
                        break

                if not is_ignore:
                    print(line.rstrip())
    except FileNotFoundError:
        print('No such file!')
