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
        '''
        returns a dictionnary of attributes attrs,
        if attrs = None returns all attributes of the class
        '''
        dict = self.__dict__
        new_dict = {}
        if attrs is not None:
            for key, value in dict.items():
                if key in attrs:
                    new_dict[key] = value
            return new_dict
        return vars(self)

    def reload_from_json(self, json):
        '''
        Sets the instance attributes to the ones in the json dic object
        '''
        for key, value in json.items():
            setattr(self, key, value)
