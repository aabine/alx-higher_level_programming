#!/usr/bin/python3

def roman_to_int(roman_string):
    """
    Returns the integer value of a roman numeral.
    Args:
        roman_string (str): roman numeral
    Returns:
        int: integer value of roman numeral
    """
    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    result = 0
    for i in range(len(roman_string)):
        if i < len(roman_string) - 1:
            if roman_dict[roman_string[i]] < roman_dict[roman_string[i + 1]]:
                result -= roman_dict[roman_string[i]]
            else:
                result += roman_dict[roman_string[i]]
        else:
            result += roman_dict[roman_string[i]]
    return result
