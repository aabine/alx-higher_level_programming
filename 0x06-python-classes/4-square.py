#!/usr/bin/python3

"""Define a class Square that defines a square"""

class Square:
    """initialize a square object"""

    def __init__(self, size=0):
        """
        Initialize a new Square.
        Args:
            size (int): The size of the new square.
        """
        self.__size = size
    @property
    def size(self):
        """ Get the size of the object. """
        return self.__size
    
    @size.setter    
    def size(self, value):
        """ Set the size of the object. """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of a square.
        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
