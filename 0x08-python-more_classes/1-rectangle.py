#!/usr/bin/python3
'''A python shebang file'''


class Rectangle:
    '''defines a rectangle'''

    def __init__(self, width=0, height=0):
        '''initializes a new rectangle class.

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        '''
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''retrieve the width of the Rectangle'''
        return (self.__width)

    @width.setter
    def width(self, value):
        '''set the width of the rectangle'''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        '''retrieve the Rectangle height'''
        return (self.__height)

    @height.setter
    def height(self, value):
        '''set the Rectangle height'''
        if not isinstance(value, int):
            raise TypeError('height must be intger')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
