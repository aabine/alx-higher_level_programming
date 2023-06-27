#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    This function takes in two arguments, a list and an integer. It iterates through the list and prints out only the integers in the list up to the specified index. If there is an error in the input, the function will continue without printing anything. Finally, it returns the count of integers that were printed.
    :param my_list: A list of integers.
    :param x: An integer specifying the index up to which the function should iterate.
    :return: An integer representing the count of integers that were printed.
    """
    count = 0
    try:
        for index in range(0, x):
            print("{:d}".format(my_list[index]), end="")
            count += 1
    except (TypeError, ValueError):
        pass
    print("")
    return count