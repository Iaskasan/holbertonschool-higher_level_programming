#!/usr/bin/python3
"""oui oui oui"""


def read_file(filename=""):
    with open(filename, 'r') as f:
        file = f.read()
        print(file)
