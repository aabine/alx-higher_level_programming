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
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
