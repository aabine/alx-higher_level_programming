#!/usr/bin/python3

def safe_print_division(a, b):
    """
    Safely divides two numbers and returns the result. If a zero division error or a value error
    occurs during the division, it returns None. The function takes two parameters:
    
    Args:
    - a (int or float): The numerator of the division.
    - b (int or float): The denominator of the division. It must not be zero.
    
    Returns:
    - float or None: The result of the division if it was successful. None otherwise.
    """

    result = 0
    try:
        result = a / b
    except (ZeroDivisionError, ValueError):
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
