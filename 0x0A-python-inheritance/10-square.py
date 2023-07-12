#!/usr/bin/python3

""" Class to define a base geometry """
Rectangle = __import__("8-rectangle").Rectangle

class Square(Rectangle):
    """ Class to define a square """
    def __init__(self, size):
        """ Initialize a new square. """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ Return the area of the square. """
        return self.__size * self.__size