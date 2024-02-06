#!/usr/bin/python3
"""defines a Square class"""


class Square:
    """This is the class Square"""
    pass

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @property
    def area(self):
        return self.size ** 2

    @size.setter
    def size(self, value):
        """This the self where you can eat"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.size == 0:
            print()
        for i in range(self.size):
            print("#" * self.size)
