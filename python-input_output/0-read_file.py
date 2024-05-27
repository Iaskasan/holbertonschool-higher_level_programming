#!/usr/bin/python3
'''Lucas m'a dit de mettre un commentaire'''


def read_file(filename=""):
    '''et ici aussi'''
    with open(filename, "r") as f:
        print(f.read(), end="")
