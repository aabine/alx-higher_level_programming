#!/usr/bin/python3

def no_c(my_string):
    """
    This function takes a string and returns
    a new string with all occurrences of "c"
    removed.
    """
    if my_string:
        n_str = ""
        for i in range(len(my_string)):
            if my_string[i] != 'c' and my_string[i] != 'C':
                n_str += my_string[i]
        return n_str