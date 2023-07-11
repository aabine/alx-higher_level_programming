#!/usr/bin/python3

""" Module that returns all attributes and methods of an object"""
def lookup(obj):
    """Returns a list of attributes and methods of the given object.

    Args:
        obj: An object to inspect.

    Returns:
        A list of strings representing the attributes and methods of the object.
    """
    return dir(obj)
