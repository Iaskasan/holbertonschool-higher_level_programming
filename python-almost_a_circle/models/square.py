#!/usr/bin/python3
"""square class file"""
from models.rectangle import Rectangle
"""square class file"""


class Square(Rectangle):
    """_summary_

    Args:
        Rectangle (_type_): _description_
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, id, x, y)
    
    @property
    def size(self):
        return self.__height
    
    @property
    def size(self):
        return self.__width
    
    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - \
{self.size}"
