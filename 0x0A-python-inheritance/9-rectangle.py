#!/usr/bin/python3

""" Class to define a base geometry """

class BaseGeometry:
    """ define a base geometry """
    def __init__(self):
        pass

    def integer_validator(self, name, value):
        """ validate if value is a positive integer """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height
    
        """Return a string representation of the rectangle."""
    def __str__(self):
        return "[{}] {}/{}".format(self.__class__.__name__,
                                       self.__width, self.__height)
