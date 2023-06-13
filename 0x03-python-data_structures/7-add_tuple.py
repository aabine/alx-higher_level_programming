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


def add_tuple(tuple_a=(), tuple_b=()):

    result = ()
    if len(tuple_a) > 0 and len(tuple_b) > 0:
        for index in range(len(tuple_a)):
            val_a = tuple_a[index] if index < len(tuple_a) else 0
            val_b = tuple_b[index] if index < len(tuple_b) else 0
            result += (val_a + val_b,)
    return result
