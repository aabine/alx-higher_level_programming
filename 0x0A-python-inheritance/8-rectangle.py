#!/usr/bin/python3

"""
Class to define a base geometry
"""

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

class Rectangle(BaseGeometry):
    """ Class to define a rectangle """
    def __init__(self, width, height):
        super().__init__()  # Call the parent class initializer
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
