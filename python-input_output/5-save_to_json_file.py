#!/usr/bin/python3
'''Bonjour à toutes et à tous'''
import json


def save_to_json_file(my_obj, filename):
    '''function that saves a file to a json object'''
    with open(filename, "w") as f:
        my_obj = json.dumps(my_obj)
        return f.write(my_obj)
