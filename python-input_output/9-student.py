#!/usr/bin/python3
'''Module for the class Student'''


class Student:
    '''class Students'''
    def __init__(self, first_name, last_name, age):
        '''the constructor'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''jason et la toison d'or'''
        return vars(self)
