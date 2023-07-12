#!/usr/bin/python3
""" A student class """

class Student:
    """class that defines a student"""
    def __init__(self, first_name, last_name, age):
        """method that initializes a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self):
        """method that returns a dictionary representation of a student"""
        return self.__dict__
