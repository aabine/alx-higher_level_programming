#!/usr/bin/python3

"""
    This function takes a list of elements and an
    index as input and returns a new list
    with the element at the given index removed.
    If the index is out of bounds, the function
    returns the original list. If the list is empty,
    the function returns the original empty list.

    Args:
        my_list (list): A list of integers to be analyzed.
        idx (int): The index of the element to be removed.

    Returns:
        list: A new list with the element at the given index removed.
"""


def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        del my_list[idx]
    return my_list
