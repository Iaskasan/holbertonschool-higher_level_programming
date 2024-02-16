#!/usr/bin/python3
"""oui oui oui"""


def read_file(filename=""):
    """_summary_

    Args:
        filename (str, optional): _description_. Defaults to "".
    """
    with open(filename, 'r') as f:
        file = f.read()
        print(file)
