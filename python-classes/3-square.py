#!/usr/bin/python3
"""building the class square"""


class Square:
    """This is the class Square

    for now its an empty classs
    """
    def __init__(self, size=0):
        """this is the constructor"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """square the size of the square and returns an int"""
        return self.__size ** 2
