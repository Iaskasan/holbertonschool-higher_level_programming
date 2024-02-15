#!/usr/bin/python3
"""module docstring"""


def inherits_from(obj, a_class):
    """docstring doc"""
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
