#!/usr/bin/python3

def no_c(my_string):
    """
    This function takes a string and returns
    a new string with all occurrences of "c"
    removed.
    """
    if my_string:
        n_str = my_string.translate({ord('c'): None, ord('C'): None})
    return n_str
