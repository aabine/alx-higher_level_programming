#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix of integers.

    Args:
        matrix: a matrix of integers

    Returns:
        None
    """
    if matrix:
        i = 0
        while i < len(matrix):
            j = 0
            while j < len(matrix[i]):
                print("{:d}".format(matrix[i][j]),
                      end=" " if j != len(matrix[i]) - 1 else "")
                j += 1
            print()
            i += 1
    else:
        print()
