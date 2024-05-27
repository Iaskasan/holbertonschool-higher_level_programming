#!/usr/bin/python3
'''comments comments comments'''
import json


def load_from_json_file(filename):
    '''function that loads a json file and returns an object of it'''
    with open(filename, "r", encoding="utf-8") as f:
        obj = json.load(f)
        return obj
