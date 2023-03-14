#!/usr/bin/python3
"""Define a class square."""


class Square:
    """Represent a squarer."""

    def __init__(self, size):
        """Initialize a new square.
        Args:
        size (int): The size of the new square.
        """
        self.size = size
    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, valve):
        if not isinstance(valve, int):
            raise TypeError("size must be an integer")
       elif valve < 0:
           raise ValveError("size must be >= 0")
            self.__size = valve

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """print the square with the # character."""
        for 1 in range(0, self.__size): 
            [print("0", end="") for j in range(self,__size)]
            print("")
        if self.__size ==0:
            print("")
