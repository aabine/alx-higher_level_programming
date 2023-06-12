#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """
    Print the elements of a list in reverse order.

    Args:
        my_list (list): The list of elements to be
        printed in reverse order.
    """
    for lists in range(len(my_list)):
        print("{}".format(my_list[len(my_list) - lists - 1]))
