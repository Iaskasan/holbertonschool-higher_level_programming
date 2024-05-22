#!/usr/bin/python3
''' Module for the method is_kind_of_class'''


def is_kind_of_class(obj, a_class):
    '''
    return True of the object is an instance of,
    or if the object is an instance of
    a class that inherited from
    '''
    return isinstance(obj, a_class)
