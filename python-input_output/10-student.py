#!/usr/bin/python3
'''Module for the class Student'''


class Student:
    '''class Students'''
    def __init__(self, first_name, last_name, age):
        '''the constructor'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''jason et la toison d'or'''
        dict = self.__dict__
        new_dict = {}
        if attrs is not None:
            for key, value in dict.items():
                if key in attrs:
                    new_dict[key] = value
            return new_dict
        return vars(self)
