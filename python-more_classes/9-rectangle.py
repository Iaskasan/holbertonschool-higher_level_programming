#!/usr/bin/python3
'''Module of the class rectangle'''


class Rectangle:
    '''Class rectangle, empty for now'''
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
        Rectangle.print_symbol = self.print_symbol

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self) -> str:
        rectangle = ""
        symbol = str(self.print_symbol) * self.width
        if self.width == 0 or self.height == 0:
            return rectangle
        for i in range(self.height):
            if i == self.height - 1:
                rectangle = f"{rectangle}{symbol}"
            else:
                rectangle = f"{rectangle}{symbol}\n"
        return rectangle

    def __repr__(self) -> str:
        parameters = f"({self.width}, {self.height})"
        class_name = type(self).__name__
        return f"{class_name}{parameters}"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1 == rect_2:
            return rect_1
        return max(rect_1, rect_2)

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)
