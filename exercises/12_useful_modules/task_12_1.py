# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
import subprocess
import ipaddress

def check_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def ping_ip_addresses(ip_list):
    alive = []
    unreachable = []

    for ip in ip_list:
#        try:
        if check_ip(ip):
            ipaddress.ip_address(ip)
            reply = subprocess.run(['ping', '-c', '3', '-n', ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if reply.returncode == 0:
                alive.append(ip)
            else:
                unreachable.append(ip)
#        except ValueError:
#            continue
    return tuple([alive, unreachable])
