#!/usr/bin/python3

class Square:
    """initialize a square object"""
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square.
        Args:
            size (int): The size of the new square.
        """
        self.size = size
        self.position = position

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
    
    def position(self):
        """ Get the position of the object. """
        return self.__position
    
    def position(self, value):
        """ Set the position of the object. """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of a square.
        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
    
    def my_print(self):
        """Prints the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
