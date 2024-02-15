#!/usr/bin/python3
"""module docstring"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """area method doc"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the types"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
