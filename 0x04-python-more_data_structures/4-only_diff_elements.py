#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    Returns the intersection of two sets.
    Args:
        set_1 (set): first set
        set_2 (set): second set
    Returns:
        set: intersection of set_1 and set_2
    Examples:
        >>> common_elements({1, 2, 3}, {3, 4, 5})
        {3}
    """
    result = None
    for element in set_1:
        if element in set_2:
            if result is None:
                result = {element}
            else:
                result = result.symmetric_difference({element})
    return result
