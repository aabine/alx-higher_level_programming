#!/usr/bin/python3

class Base:
    """ private class attribute """
    __nb_objects = 0
    def __init__(self, id = None):
        """ class method or constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    