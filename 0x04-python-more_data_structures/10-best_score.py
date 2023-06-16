#!/usr/bin/python3

def best_score(a_dictionary):
    """
    Returns the key with the highest value in a dictionary.
    """
    if a_dictionary:
        lop_list = list(a_dictionary.keys())
        best_score = 0
        str_primary = ''
        for i in lop_list:
            if a_dictionary[i] > best_score:
                best_score = a_dictionary[i]
                str_primary = i
        return str_primary
