#!/usr/bin/python3
def common_elements(set_1, set_2):
    """
    Returns the intersection of two sets.
    Args:
        set_1 (set): first set
        set_2 (set): second set
    Returns:
        set: common elements of set_1 and set_2

    Examples:
        >>> common_elements({1, 2, 3}, {3, 4, 5})
        {3}
    """
    return set_1.intersection(set_2)
