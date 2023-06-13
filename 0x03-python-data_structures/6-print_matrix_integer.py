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
        for m_row in range(len(matrix)):
            for m_el in range(len(matrix[m_row])):
                print("{:d}".format(matrix[m_row][m_el]), end=" ")
            print()
    else:
        print()
