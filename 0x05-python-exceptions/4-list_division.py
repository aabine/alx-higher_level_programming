#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
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
        for index in range(list_length):
            result = my_list_1[index] / my_list_2[index]
    except (ZeroDivisionError, ValueError):
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
