#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    Returns a list of lists of integers
    square_matrix_simple(matrix)

    Args:
        matrix (list): list of lists

    Returns:
        list: list of lists of integers
    """
    if not matrix:
        return []
    s_matrix = []

    for row in matrix:
        s_row = []
        for element in row:
            s_element = element ** 2
            s_row.append(s_element)
        s_matrix.append(s_row)
    return s_matrix
