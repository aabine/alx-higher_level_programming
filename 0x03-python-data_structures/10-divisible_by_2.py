#!/usr/bin/python3

"""
    This function takes a list of integers as input and returns a new list
    containing only the even numbers in the original list. If the original
    list is empty, the function returns the original list.

    Args:
        my_list (list): A list of integers to be analyzed.

    Returns:
        list: A new list containing only the even numbers in the original list.
    """


def divisible_by_2(my_list=[]):
    if my_list:
        n_list = []
        for index in range(len(my_list)):
            if my_list[index] % 2 == 0:
                n_list.append(True)
            else:
                n_list.append(False)
        return n_list
    else:
        return my_list
