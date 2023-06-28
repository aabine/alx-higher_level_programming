def list_division(my_list_1, my_list_2, list_length):
    """
    Safely divides two numbers and returns the result. If a zero division error or a value error
    occurs during the division, it returns None. The function takes two parameters:

    Args:
    - my_list_1 (list): The numerator of the division.
    - my_list_2 (list): The denominator of the division. It must not be zero.

    Returns:
    - list: The results of the division. Each element in the list corresponds to the division of the corresponding elements from my_list_1 and my_list_2. If an error occurs during the division, the corresponding element in the result list is None.
    """

    results = []
    for index in range(list_length):
        try:
            result = my_list_1[index] / my_list_2[index]
        except ZeroDivisionError:
            result = 0
        except (ValueError, IndexError, AttributeError):
            result = 0
        except TypeError:
            result = 0
        finally:
            results.append(result)
    return results
