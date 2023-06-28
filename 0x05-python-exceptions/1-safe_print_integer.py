#!/usr/bin/python3

def safe_print_integer(value):
    """
    Checks if the input value is an integer. If it is,
    it prints the value without a newline,
    and returns True. If it is not, returns False. 
    
    :param value: The input value to be checked.
    :type value: int
    
    :return: True if the input value is an integer, False otherwise.
    :rtype: bool
    """

    try:
        if isinstance(value, int):
            print("{:d}".format(value), end="")
            return True
    except (TypeError, ValueError):
        return False
