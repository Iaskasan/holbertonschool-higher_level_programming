#!/usr/bin/python3
"""this script write a class Square that defines a square """


class Square:
    """this class defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) and len(value) == 2 \
                and all(isinstance(elem, int) and elem >= 0 for elem in value):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(0, self.size):
                for _ in range(self.position[0]):
                    print(" ", end='')
                for _ in range(self.size):
                    print("#", end='')
                print()

    def __str__(self):
        square = ""
        symbol = '#' * self.size
        position = " " * self.position[0]
        if not self.size or self.position[1] > 0:
            square = '\n'
        for i in range(self.size):
            if i == self.size - 1:
                square = f"{square}{position}{symbol}"
            else:
                square = f"{square}{position}{symbol}\n"
        return square
