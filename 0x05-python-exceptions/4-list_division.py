#!!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
"""Divides two lists element by element.

    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The number of elements to divide.

    Returns:
        A new list of length list_length containing all the divisions.
    """

    results = []
    for index in range(0, list_length):
        try:
            result = my_list_1[index] / my_list_2[index]
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except (IndexError):
            print("out of range")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        finally:
            results.append(result)
    return results
