#!/usr/bin/python3
'''Adonis le plus beau'''
from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


python_list = []
try:
    python_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    pass
finally:
    for args in argv[1:]:
        python_list.append(args)
    save_to_json_file(python_list, "add_item.json")
