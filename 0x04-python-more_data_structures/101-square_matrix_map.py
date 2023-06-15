#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    """
    Returns a list of lists of integers
    square_matrix_map(matrix)

    Args:
        matrix (list): list of lists

    Returns:
        list: list of lists of integers
    """
    if not matrix:
        return []
    s_matrix = []
    s_matrix = list(map(lambda x: list(map(lambda y: y ** 2, x)), matrix))
    return s_matrix