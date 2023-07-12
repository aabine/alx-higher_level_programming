#!/usr/bin/python3
""" interview question """
def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the given number of rows.

    Args:
        n (int): The number of rows to generate in Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []
    
    triangle = []

    for i in range(n):
        row = [1]

        if i > 0:
            prev_row = triangle[i-1]
            for j in range(1, i):
                row.append(prev_row[j-1] + prev_row[j])

            row.append(1)

        triangle.append(row)

    return triangle
