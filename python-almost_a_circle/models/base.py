#!/usr/bin/python3
"""base class file"""
from json import dumps, loads, dump, load


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

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        filename = f"{cls.__name__}.json"
        lists_dict = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as f:
            f.write(cls.to_json_string(lists_dict))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            string = json_string = []
        else:
            string = loads(json_string)
        return string

    @classmethod
    def create(cls, **dictionary):
        instance = cls(4, 1)
        instance.update(**dictionary)
        return instance
