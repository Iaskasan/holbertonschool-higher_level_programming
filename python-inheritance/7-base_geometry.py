#!/usr/bin/python3
'''Module for the class BaseGeometry'''


class BaseGeometry:
    '''Class BaseGeometry'''
    def area(self):
        '''raise an exception for now'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''method that validates and int'''
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        return True
