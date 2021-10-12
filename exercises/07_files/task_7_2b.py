# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

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
        config_clear = []

        for line in file:
            is_ignore = False
            for item in ignore:
                if line.count(item) > 0:
                    is_ignore = True
                    break

            if not is_ignore and not line.startswith('!'):
                config_clear.append(line.rstrip())

        with open(argv[2],'w') as f:
            f.writelines(l + '\n' for l in config_clear)

    except FileNotFoundError:
        print('No such file!')
