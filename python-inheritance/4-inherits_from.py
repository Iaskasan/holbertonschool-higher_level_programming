#!/usr/bin/python3
'''this is the module for the inherits_from method'''


def inherits_from(obj, a_class):
    '''
    return True if the object
    is a subclass of the class a_class
    '''
    return issubclass(obj, a_class)
