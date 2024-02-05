#!/usr/bin/python3
from typing import overload
"""defines a Square class"""


class Square:
    """This is the class Square"""
    pass

    def __init__(self, size=0):
        """This the self where you can eat"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
