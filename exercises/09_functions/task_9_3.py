# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов,
  а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов,
  а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
def get_int_vlan_map(config_filename):
    with open(config_filename) as f:
        port_trunk = {}
        port_access = {}

        file_lines = f.readlines()
        interface = ''

        for line in file_lines:
            if line.startswith('interface'):
                interface = line.split()[-1].strip()
            elif line.startswith('!'):
                interface = ''
            elif line.find('access vlan') != -1  and interface:
                port_access[interface] = int(line.split()[-1].strip())
            elif line.find('trunk allowed vlan') != -1  and interface:
                port_trunk[interface] = [int(vlan) for vlan in line.split()[-1].strip().split(',')]

    return tuple([port_access, port_trunk])

result = get_int_vlan_map('config_sw1.txt')

print(result)
