#!/usr/bin/python3

from models.rectangle import Rectangle


class Square(Rectangle):
    '''A square class that inherites fron the Rectangle class'''

    def __init__(self, size, x=0, y=0, id=None):
        '''the constructor of the square class
        Args:
            size (int): the size of square
            x (int, optional): the x coordinate (default is 0)
            y (int, optional): the y coordinate (default is 0)
            id (int, optional): the object identifier (default is 0)
        '''
        super().__init__(size, size, x=0, y=0, id=None)

        def __str__(self):
            '''overloaded __str__ methid to represent the
            square object as a string
            Return:
                str: representation of the sqquare object
            '''
            return "[square] ({}) {}/{} - {}".format(self.id,
                                                self.x,
                                                self.y,
                                                self.width)
