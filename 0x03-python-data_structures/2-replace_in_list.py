#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """
    Replace an element at a specific index in a list.

    Args:
        my_list (list): The list of elements.
        idx (int): The index where the element should be replaced.
        element: The new element to be placed at the specified index.

    Returns:
        The modified list with the element replaced,
        or the original list if the index is invalid.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
