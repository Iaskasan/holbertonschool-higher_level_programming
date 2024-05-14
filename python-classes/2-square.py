#!/usr/bin/python3
"""building the class square"""


class Square:
    """This is the class Square

    for now its an empty classs
    """
    def __init__(self, size=0):
        """this is the constructor"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
