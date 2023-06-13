#!/usr/bin/python3

def multiple_returns(sentence):
    """
    Returns a tuple containing the length of the input
    string and its first character, or a tuple containing a single value
    of zero if the input string is empty.

    Parameters:
    sentence (str): A string to be analyzed.

    Returns:
    tuple: A tuple containing the length of the input string
    and its first character, or a tuple containing a single value
    of zero if the input string is empty.

    """
    if sentence:
        length = len(sentence)
        first_char = sentence[0]
        return length, first_char
    else:
        return 0, "None"
