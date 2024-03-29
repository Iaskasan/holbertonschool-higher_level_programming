#!/usr/bin/python3
"""module docstring"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """area method doc"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the types"""
        if type(value) is not (int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
