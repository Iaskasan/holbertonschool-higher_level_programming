#!/usr/bin/python3
'''
module for the method lookup that returns a list of
all attributes and and methods of an object
'''


def lookup(obj):
    '''returns a list of method and attr of an obj'''
    return dir(obj)
