#!/usr/bin/python3
'''This is a module for the abstract class Shape'''
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    '''Abstract class Shape'''
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    '''Class Circle that inherits from the abstract class Shape'''
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius


class Rectangle(Shape):
    '''Class Rectangle that inherits from the abstract class Shape'''
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return (self.height + self.width) * 2


def shape_info(shape):
    print(shape.area())
    print(shape.perimeter())
