#!/usr/bin/python3
"""base class file"""
from json import dumps, loads


class Base:
    """class Based"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """faut pas copier les githubs"""
        if list_dictionaries is None:
            return "[]"
        else:
            return dumps(list_dictionaries)
