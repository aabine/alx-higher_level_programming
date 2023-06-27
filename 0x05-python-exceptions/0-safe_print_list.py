#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    This function prints a specified number of elements from a given list.
    If the number of elements to be printed is greater than the length of
    the list, the entire list is printed. The function returns the number
    of elements printed.

    :param my_list: A list of elements to be printed.
    :param x: An integer specifying the number of elements to be printed.
    :return: An integer representing the number of elements printed.
    """
    count = 0
    
    try:
        for index in range(x):
            print("{}".format(my_list[index]), end="")
            count += 1
    except IndexError:
            print(my_list)
    return count
