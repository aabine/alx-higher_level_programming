#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """
    This function prints a matrix of integers.

    Args:
        matrix: a matrix of integers

    Returns:
        Nothing
    """
    if matrix:
        for m_row in matrix:
            for m_el in m_row:
                print("{}".format(m_el), end=" ")
            print()