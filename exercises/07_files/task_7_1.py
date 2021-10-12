# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
try:
    with open('ospf.txt', 'r') as f:
        for line in f:
            line_list = line.split()
            if len(line_list) > 3: line_list.pop(3)

            line_list[0] = (lambda x: 'OSPF' if x == 'O' else x)(line_list[0])
            line_list[2] = line_list[2].replace('[','').replace(']','')
            line_list[3] = line_list[3][:-1]
            line_list[4] = line_list[4][:-1]

            caption = ['Protocol','Prefix','AD/Metric','Next-Hop','Last update','Outbound Interface']

            for name, item in zip(caption[1:], line_list[1:]):
                print('{:20} {:20}'.format(name, item))
            print('\n')
except FileNotFoundError:
    print('No such file!')
