#!/usr/bin/python3
"""oui oui oui"""


class Student:
    """class Student doc"""
    def __init__(self, first_name, last_name, age):
        self.fname = first_name
        self.lname = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
