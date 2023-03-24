#!/usr/bin/python3
"""defines class Square that inherits from Rectangle"""


Rectangle = _import_('9-rectangle').Rectangle


class Square(Rectangle):
    """class for square that inherits from Rectangle
    with method for area"""
    def _init_(self, size):
        """initializes Square instance"""
        self.integer_validator("size", size)
        self.__size = size
        super()._init_(size, size)

    def area(self):
        """returns area of square"""
        return (self.__size * self.__size)
