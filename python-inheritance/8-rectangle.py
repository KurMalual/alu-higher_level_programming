#!/usr/bin/python3
"""defines class Rectangle that inherits from BaseGeometry"""


BaseGeometry = _import_('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class for rectangle that inherits from BaseGeometry"""
    def _init_(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
