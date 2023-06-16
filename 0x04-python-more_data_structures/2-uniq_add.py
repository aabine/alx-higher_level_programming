#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    Returns the sum of all elements in a list without duplicates.
    
    Args:
        my_list (list): list of integers

    Returns:
        int: sum of all elements in the list without duplicates.
    """
    listResult = []
    sum_result = 0
    for element in my_list:
        if element not in listResult:
            sum_result += element
            listResult.append(element)
    return sum_result
