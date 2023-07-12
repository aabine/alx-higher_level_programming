#!/usr/bin/python3
""" Define a function that returns True if the object is exactly an instance of the specified class. """
def is_direct_subclass_of(obj, a_class):
    """
    Checks if an object is a direct subclass of a given class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if the object is a direct subclass of the class, False otherwise.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
