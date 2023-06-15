#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    # Create a list to store the keys to be deleted
    keys_to_delete = []

    # Iterate over the key-value pairs in the dictionary
    for key, val in a_dictionary.items():
        if val == value:
            keys_to_delete.append(key)

    # Delete the keys from the dictionary
    for key in keys_to_delete:
        del a_dictionary[key]

    return a_dictionary
