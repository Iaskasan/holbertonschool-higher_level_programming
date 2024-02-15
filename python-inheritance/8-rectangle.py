#!/usr/bin/python3
"""module docstring"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class kek"""
    def __init__(self, width, height):
        """docstring checker"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
