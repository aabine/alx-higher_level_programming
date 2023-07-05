#!/usr/bin/python3

def max_integer(list=[]):
    """
    Find and return the maximum integer from a given list.

    Parameters:
    - list (list): The list from which the maximum integer needs to be found.

    Returns:
    - int or None: The maximum integer from the given list. If the list is empty, returns None.

    Raises:
    - TypeError: If the input list is not of type list.
    """

    if not isinstance(list, list):
        raise TypeError("list must be a list")
    if len(list) == 0:
        return None
    while len(list) > 0:
        max = list[0]
        for i in list:
            if i > max:
                max = i
        list.remove(max)
        return max
