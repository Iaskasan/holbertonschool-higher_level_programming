#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key, val in a_dictionary.items():
        if val != value:
            continue
        else:
            a_dictionary.pop(key)
            return complex_delete(a_dictionary, value)
    return a_dictionary
