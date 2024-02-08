#!/usr/bin/python3
"""defines a Square class"""


class Square:
    """This is the class Square"""
    pass

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @property
    def area(self):
        return self.size ** 2

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        """This the self where you can eat"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if not isinstance(value, (tuple, int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        first_element = self.position[0]
        if not self.size:
            print()
        for j in range(self.position[1]):
            print()
        for i in range(self.size):
            print(" " * first_element + "#" * self.size)
