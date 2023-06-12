#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """
    Print the elements of a list in reverse order.

    Args:
        my_list (list): The list of elements to be
        printed in reverse order.
    """
    rev_list = list(reversed(my_list))
    for lists in rev_list:
        print("{}".format(lists))
