#!/usr/bin/python3

def is_kind_of_class(obj, a_class):
    """Return true if the object is exactly an instance of the specified class. """
    if isinstance(obj, a_class):
        return True
    else:
        return False
