#!/usr/bin/python3

def best_score(a_dictionary):
    """
    Returns the key with the highest value in a dictionary.
    """
    if not a_dictionary:
        return None
    best = None
    for key in a_dictionary:
        if best is None or a_dictionary[key] > best:
            best = a_dictionary[key]
    return best
