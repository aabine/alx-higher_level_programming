#!/usr/bin/python3
""" script that returns json representation of an object(string) """
import json

def to_json_string(my_obj):
    """function that returns json representation of an object(string)"""
    return json.dumps(my_obj)
