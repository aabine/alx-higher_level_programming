#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of the matrix by the given divisor.

    Args:
        matrix (list of lists): The matrix to be divided.
        div (int or float): The divisor.

    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats, or if any row in the matrix has a different size.
        ZeroDivisionError: If the divisor is zero.

    Returns:
        list of lists: A new matrix with each element divided by the divisor, rounded to 2 decimal places.
    """
    # Check if matrix is a list of lists containing integers or floats
    if not all(isinstance(row, list) and all(isinstance(ele, (int, float)) for ele in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row has the same size
    row_sizes = set(len(row) for row in matrix)
    if len(row_sizes) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check for division by zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform the division and rounding to 2 decimal places
    result_matrix = [[round(ele / div, 2) for ele in row] for row in matrix]

    return result_matrix
