#!/usr/bin/python3
def find_peak(list_of_integers):
    """
    Finds the peak element in a given list of integers.

    Parameters:
        list_of_integers (List[int]): A list of integers.

    Returns:
        int: The peak element in the list.

    """
    if not list_of_integers:
        return None

    left = 0
    right = len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]
