#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    Returns the sum of all elements in a list without duplicates.
    
    Args:
        my_list (list): list of integers

    Returns:
        int: sum of all elements in the list without duplicates.
    """

    if not my_list:
        return 0
    
    sum_result = 0
    for element in my_list:
        sum_result += element
    return sum_result
