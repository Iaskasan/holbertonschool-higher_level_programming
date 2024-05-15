#!/usr/bin/python3
"""building the class square"""


class Square:
    """This is the class Square

    The class is not yet complete
    """
    def __init__(self, size=0, position=(0, 0)):
        """this is the constructor"""
        self.__size = size
        self.position = position

    def area(self):
        """square the size of the square and returns an int"""
        return self.__size ** 2

    @property
    def size(self):
        '''class method to retrieve or modify the value of size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''checks if the input is an int and > 0'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        '''prints the square with "#" as character'''
        if self.size == 0:
            print()
        for _ in range(self.size):
            if self.position[1] > 0:
                self.position[0] == 0
            print(" " * self.position[0] + "#" * self.size)

    @property
    def position(self):
        """"""
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) and len(value) == 2\
                and all(isinstance(element, int) for element in value):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
