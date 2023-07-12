#!/usr/bin/python3

""" A function that returns True if it's object """
def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance of a class.
    """
    if type(obj) == a_class:
        return True
    else:
        return False
