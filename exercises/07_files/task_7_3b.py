# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
vlan_no = input('Enter VLAN: ')
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
                if line_list[0] == vlan_no:
                    cam_to_write.append([int(line_list[0]), line_list[1], line_list[3]])

    cam_to_write.sort()
    for row in cam_to_write:
        print('{:<15} {:<15} {:<15}'.format(*row))
except IOError:
    print('No such file!')
