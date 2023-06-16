#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """
    Deletes the given key in the given dictionary if it exists. I
    don't check if the key is not
    in the dictionary, the dictionary remains unchanged.
    
    
    :param a_dictionary: A dictionary to delete the key from (dict).
    :param key: The key to delete (optional) (Any).
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
