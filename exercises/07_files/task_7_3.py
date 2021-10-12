# -*- coding: utf-8 -*-
"""
Задание 7.3

Скрипт должен обрабатывать записи в файле CAM_table.txt. Каждая строка,
где есть MAC-адрес, должна быть обработана таким образом, чтобы
на стандартный поток вывода была выведена таблица вида:

100      01bb.c580.7000      Gi0/1
200      0a4b.c380.7c00      Gi0/2
300      a2ab.c5a0.700e      Gi0/3
10       0a1b.1c80.7000      Gi0/4
500      02b1.3c80.7b00      Gi0/5
200      1a4b.c580.7000      Gi0/6
300      0a1b.5c80.70f0      Gi0/7
10       01ab.c5d0.70d0      Gi0/8
1000     0a4b.c380.7d00      Gi0/9


Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
try:
    with open('CAM_table.txt','r') as f:
        cam_table = f.readlines()

    mac_order = {'0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'}
    cam_to_write = []

    for line in cam_table:
        line_list = line.strip().split()
        is_mac = False

        for str_line in line_list:
            mac_addr = str_line.split('.')
            if len(mac_addr) == 3:
                is_mac = True

                for oktet in mac_addr:
                    for char in oktet:
                        if not char in mac_order:
                            is_mac = False
                            break

                    if not is_mac:
                        break

        if is_mac:
            if len(line_list) == 4:
                cam_to_write.append(line_list[0] + ' ' + line_list[1] + ' ' + line_list[3])

    for row in cam_to_write:
        print('{:15} {:15} {:15}'.format(*row.split()))
except IOError:
    print('No such file!')
