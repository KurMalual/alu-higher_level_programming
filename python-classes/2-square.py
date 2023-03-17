#!/usr/bin/python3
"""A class that defines a square"""


class Square:
    """Create a square.
    Private instance attributes: size
    """

    def _init_(self, size=0):
        """Initializes date."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
