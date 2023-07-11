#!/usr/bin/python3

""" Module that returns all attributes and methods of an object"""                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
class mylist(list):
    def __init__(self):
        super().__init__()

def print_sorted(self):
    """Prints the list, but sorted in ascending order."""
    print(sorted(self))
