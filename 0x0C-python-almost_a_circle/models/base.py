#!/usr/bin/python3
class Base():
    '''Base class for model objects
    Attributes:
        __nb_objects (int): a private class attribute
        to track number of objects
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''
        The base class constructor
        Args:
            id (int, optional): an identifier for the object
            if provided assigns it, otherwise __nb_objects is
            incremented and assigned to id
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
