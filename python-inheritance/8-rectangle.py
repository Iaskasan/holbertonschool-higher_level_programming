#!/usr/bin/python3
'''Module for the class BaseGeometry'''


class BaseGeometry:
    '''Class BaseGeometry'''
    def area(self):
        '''raise an exception for now'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''method that validates and int'''
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        return True


class Rectangle(BaseGeometry):
    '''class Rectangle that inherits from class BaseGeometry'''
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

if __name__ == "__main__":
    r = Rectangle(3, 5)

    print(r)
    print(dir(r))

    try:
        print("Rectangle: {} - {}".format(r.width, r.height))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r2 = Rectangle(4, True)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))