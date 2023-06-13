#!/usr/bin/python3

def max_integer(my_list=[]):
    """
    Returns the maximum integer value in the input list.

    Parameters:
    my_list (list): A list of integers to be analyzed.

    Returns:
    int or None: The maximum integer value in the input list,
    or None if the input list is empty.

    """
    if my_list:
        max_output = my_list[0]
        for index in my_list:
            if index > max_output:
                max_output = index
        return max_output
    else:
        return None
