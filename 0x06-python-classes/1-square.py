#!/usr/bin/python3
"""Define a class Square that defines a square"""
class Square:
    """initialize a square object"""

    def __init__(self, size=0):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size
