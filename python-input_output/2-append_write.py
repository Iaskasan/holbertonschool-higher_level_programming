#!/usr/bin/python3
'''module for the function append on a file'''


def append_write(filename="", text=""):
    '''function that appends text in a file'''
    with open(filename, "a") as f:
        f.write(text)
        return len(text)
