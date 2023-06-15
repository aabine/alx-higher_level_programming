#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """
    Updates a dictionary with a key-value pair. If the key already exists in the dictionary,
    the function appends the new value to the list of values associated with the key. If the
    key does not exist in the dictionary, a new key-value pair is added to the dictionary.
    
    :param a_dictionary: A dictionary to be updated. (dict)
    :param key: A key for the dictionary. (any hashable type)
    :param value: A value to be associated with the key. (any type)
    
    :return: None
    """
    if key in a_dictionary:
        a_dictionary[key].append(value)
    else:
        a_dictionary[key] = [value]
    