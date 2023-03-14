#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init_(self, size=0):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
            """
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValveError("size must be >= 0")
            self,__size = size
