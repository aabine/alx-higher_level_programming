#!/usr/bin/python3
""" create and a function that adds attributes """
def hasattr(obj, name, value):
    """ Check if an object has a given attribute """
    if not hasattr(obj, __dict__):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
