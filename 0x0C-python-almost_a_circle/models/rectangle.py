#!/usr/bin/bash
'''A python shebang script'''

from models.base import Base


class Rectangle(Base):
    '''defines a rectangle class'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''The Rectangle class constructor
        Args:
            width (int, float): the rectangle width
            height (int, float): the rectangle height
            x (int, float): the x coordinate
            y (int, float): thr y coordinate
            id (int, optional): the identifier for objects
        '''
        super().__init__(id)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        '''getter method
        Return:
            width value
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''setter method
        Args:
            value: the new value
        '''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        '''getter method
        Return:
            height value
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''setter method
        Args:
            value: the new value
        '''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        '''getter method
        Return:
            x value
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''setter method
        Args:
            value: the new value
        '''
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        '''getter method
        Return:
            y value
        '''
        return self.__y

    @y.setter
    def y(self, value):
        '''setter method
        Args:
            value: the new value
        '''
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        '''computes area of Rectangle object
        Return:
            computed result
        '''
        return self.__width * self.__height

    def display(self):
        '''displays to stdout the rectangle object using "#"
            and representing the x and y coordinats'''
        for _ in range(self.y):
            print()
        for _ in range(self.__height):
            print(' ' * self.x + '#' * self.__width)

    def __str__(self):
        '''prints a readable/customized object
            format; can be reusable'''

        return ('[Rectangle] ({}) {}/{} {}/{}'
                .format(self.id,
                        self.x,
                        self.y,
                        self.width,
                        self.height))

    def update(self, *args, **kwargs):
        '''updates attribute of the rectangular instance
        based on arbitrary argumenns
        Args:
            *args: arbitrary positional arguments
            **kwargs: key word positional argument
        '''

        if args:
            if len(args) >= 1:
                self.id = args[0]

            if len(args) >= 2:
                self.width = args[1]

            if len(args) >= 3:
                self.height = args[2]

            if len(args) >= 4:
                self.x = args[3]

            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
