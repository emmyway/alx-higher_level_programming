#!/usr/bin/python3
'''A python shebang file'''


class Rectangle:
    '''defines a rectangle

    Attribute:
        number_of_instance (int): the present numbrr of rectangle instance
        print_symbol (any): the symbol used for string representation
    '''

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''initializes a new rectangle class.

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        '''
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1
        # same as type(self).number_of_reftangle

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
            raise TypeError('height must be an intger')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        '''return the area of rectangle'''
        return (self.__width * self.__height)

    def perimeter(self):
        '''return perimeter of rectangle'''
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        '''return the string representation of a class'''
        return '\n'.join(['#' * self.__width] * self.__height)

    def __repr__(self):
        '''return an informal or a custom representation of objects'''
        return f"Rectangle({self.__width}, {self.height})"

    def __del__(self):
        '''print a mesaage after every deletion'''
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Reftangle')

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
