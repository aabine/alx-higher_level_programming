#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """
    This function takes a list, an index,
    and an element as arguments.
    It returns a new list with the element at the specified index.
    The original list is not modified.
    """
    if my_list:
        if idx < 0 or idx > len(my_list):
            return my_list
        n_list = my_list.copy()
        n_list[idx] = element
    return n_list
