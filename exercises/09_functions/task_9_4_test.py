#!/usr/bin/env python3
# -*- coding: utf-8 -*-
ignore = ["duplex", "alias", "configuration"]

def ignore_command(command, ignore):
    ignore_status = False
    for word in ignore:
        if word in command:
            ignore_status = True
    return ignore_status

def convert_config_to_dict(config_filename):
    result = {}
    key = ''

    with open(config_filename) as f:
        file_lines = f.readlines()

        for line in file_lines:
            if not ignore_command(line, ignore) and not line.startswith('!') and len(line.strip()) > 0:
                if line.startswith(' '):
                    if result.get(key, 'Not exists') != 'Not exists':
                        result[key].append(line.strip())
                else:
                    key = line.strip()
                    result[key] = []

    return result

dict = convert_config_to_dict('config_sw1.txt')
print(dict)
