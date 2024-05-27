#!/usr/bin/python3
'''Module for the function that write in a file'''


def write_file(filename="", text=""):
    '''writes in a file'''
    with open(filename, "w") as f:
        return f.write(text)
