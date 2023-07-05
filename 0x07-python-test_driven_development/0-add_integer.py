#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Add two integers and return the result.
    Args:
        a (int): The first integer
        b (int): The second integer
    Returns:
        int: The sum of a and b
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
