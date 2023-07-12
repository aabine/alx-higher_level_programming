#!/usr/bin/python3

""" Class to define a base geometry """
class BaseGeometry:
    """ define a base geometry """
    def area(self):
        """ raise an exception """
        raise Exception("area() is not implemented")

def integer_validator(self, name, value):
    """
    Validate if the given value is an integer and greater than 0.

    Parameters:
        name (str): The name of the value being validated.
        value (int): The value to be validated.

    Raises:
        TypeError: If the value is not an integer.
        ValueError: If the value is less than or equal to 0.
    """
    if type(value) != int:
        raise TypeError("{} must be an integer".format(name))
    if value <= 0:
        raise ValueError("{} must be greater than 0".format(name))
