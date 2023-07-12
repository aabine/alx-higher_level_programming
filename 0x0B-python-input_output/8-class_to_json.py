#!/usr/bin/python3
""" python class to dictionary script """

def class_to_json(obj):
    """function that returns a dictonary description of a simple data structure"""
    return obj.__dict__
