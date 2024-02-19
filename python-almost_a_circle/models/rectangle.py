#!/usr/bin/python3
"""rectangle class file"""
from base import Base
"""rectangle class file"""


class Rectangle(Base):
    """class Rectangle doc"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """rectangle class file"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """rectangle class file"""
        return self.__width

    @property
    def height(self):
        """rectangle class file"""
        return self.__height

    @property
    def x(self):
        """rectangle class file"""
        return self.__x

    @property
    def y(self):
        """rectangle class file"""
        return self.__y

    @width.setter
    def width(self):
        """rectangle class file"""
        pass

    @height.setter
    def height(self):
        """rectangle class file"""
        pass

    @x.setter
    def x(self):
        """rectangle class file"""
        pass

    @y.setter
    def y(self):
        """rectangle class file"""
        pass
