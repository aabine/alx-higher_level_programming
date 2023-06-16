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
    
    mapped_matrix = []
    mapped_matrix = [list(map(lambda x: x ** 2, row)) for row in matrix]
    return mapped_matrix