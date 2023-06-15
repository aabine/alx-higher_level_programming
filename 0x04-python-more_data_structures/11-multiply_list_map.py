#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    """
    Takes a list of integers `my_list` and a number `number` as parameters,
    multiplies each number in `my_list` by `number` using `map()` function,
    and returns the resulting list.

    :param my_list: A list of integers.
    :param number: An integer to multiply each element in `my_list` by.
    :return: A list of integers resulting from the multiplication.
    """
    result = list(map(lambda x: x * number, my_list))
    return result
