#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """
    Multiplies each value in a_dictionary by 2.
    
    :param a_dictionary: A dictionary with keys and values to be multiplied by 2.
    :type a_dictionary: dict
    
    :return: A dictionary with the same keys as a_dictionary and values that are twice as large.
    :rtype: dict
    """
    for key in a_dictionary:
        a_dictionary[key] *= 2
    return a_dictionary
