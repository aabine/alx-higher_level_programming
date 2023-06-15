#!/usr/bin/python3

def weight_average(my_list=[]):
    """
    Returns the weighted average of all elements in a list.
    Args:
        my_list (list): list of integers
    Returns:
        int: weighted average of all elements in the list
    """
    if not my_list:
        return 0
    sum_result = 0
    for element in my_list:
        sum_result += element[0] * element[1]
    return sum_result / sum([element[1] for element in my_list])
