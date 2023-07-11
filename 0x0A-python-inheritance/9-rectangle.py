#!/usr/bin/python3

""" Class to define a base geometry """

BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
    """ 
    A Class to define a rectangle

    Attributes:
        width (int): width of the rectangle
        height (int): height of the rectangle

    Methods:
        __init__(self, width, height)
        integer_validator(self, name, value)
    """
    def __init__(self, width, height):
        """Initialize a Rectangle object with given width and height."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
        
    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height
    
    def __str__(self):
        """Return a string representation of the rectangle."""
        def __str__(self):
            return "[{}] {}/{}".format(self.__class__.__name__,
                                       self.__width, self.__height)
