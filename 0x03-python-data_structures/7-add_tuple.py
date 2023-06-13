#!/usr/bin/python3

"""
This module contains a function that adds two tuples.

This function takes two tuples and adds them together
and returns the result.

Args:
    tuple_a: a tuple of integers
    tuple_b: a tuple of integers

Returns:
    a tuple of integers
"""


def add_tuple(tuple1=(), tuple2=()):
    # Add two tuples
    padded_tuple1 = tuple1 + (0, 0)
    padded_tuple2 = tuple2 + (0, 0)

    # Compute the sum
    sum_x = padded_tuple1[0] + padded_tuple2[0]
    sum_y = padded_tuple1[1] + padded_tuple2[1]

    # Return the sum
    sum_tuple = (sum_x, sum_y)

    return sum_tuple
