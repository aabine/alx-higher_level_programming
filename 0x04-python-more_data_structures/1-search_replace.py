#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    Takes in a list 'my_list' and two arguments 'search' and 'replace'.
    Searches for all occurrences of 'search'
    in 'my_list' and replaces it with 'replace'
    and returns a new list 'l_result' with the replaced values. 

    :param my_list: a list of elements.
    :param search: an element to search for in the list.
    :param replace: an element to replace 'search' with in the list.
    :return: a new list with replaced values.
    """
    l_result = []
    for lc in range(len(my_list)):
        if my_list[lc] == search:
            my_list[lc] = replace
        l_result.append(my_list[lc])
    return l_result
