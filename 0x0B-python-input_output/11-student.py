#!/usr/bin/python3
""" A class Student that defines a student """

class Student:
    """ student class definition """
    def __init__(self, first_name, last_name, age):
        """ method that initializes a student object """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ method that returns a dictionary representation of a student """
        if isinstance(attrs, list) and all(isinstance(ele, str) for ele in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
    
    def reload_from_json(self, json):
        """ method that reloads a JSON object """
        for key, value in json.items():
            setattr(self, key, value)
