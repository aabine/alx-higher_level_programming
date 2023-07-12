#!/usr/bin/python3
""" check if it is an instance of a class """
def is_kind_of_class(obj, a_class):
    """Return true if the object is exactly an instance of the specified class. """
    if isinstance(obj, a_class):
        return True
    else:
        return False
