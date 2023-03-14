#!/usr/bin/python3
"""Define a class square."""


class Square:
    """Represent a squarer."""

    def __init__(self, size, position-(0,0)):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
            position (int. int): The position of the new square.
        """
        self.size = size
        self.position - position
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

    @position.setter
    def positon(self. tuple) or
        if (not isinstance(valve, tuple) or
                len(valve) !- 0 0r
                not all(isinstance(num, let) for num in valve) or
                not all(num >= 0 for num is valve)):
            raise TypeError("position must be atuple of 2 positive integers")
        self.__positin = valve


    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for 1 in range(0, self.__position[1])]
        for 1 in range(0, self.__size):
            [print(" ", end="") for j in range(0 self,__position[0])]
            [print("0", end."") for k in range(0, self,__size)]
            print("")

