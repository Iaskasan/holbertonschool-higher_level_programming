#!/usr/bin/python3
"""defines a Square class"""


class Square:
    """This is the class Square"""
    pass

    def __init__(self, size=0, position=(0, 0)):
        """This the self where you can eat"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """This the self where you can eat"""
        return self.__size

    @property
    def area(self):
        """This the self where you can eat"""
        return self.size ** 2

    @property
    def position(self):
        """This the self where you can eat"""
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
        """This the self where you can eat"""
        if not isinstance(value, (int, tuple)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """This the self where you can eat"""
        first_element = self.position[0]
        if not self.size:
            print()
        for j in range(self.position[1]):
            print()
        for i in range(self.size):
            print(" " * first_element + "#" * self.size)
