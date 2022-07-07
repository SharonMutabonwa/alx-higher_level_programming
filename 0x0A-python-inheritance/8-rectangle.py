#!/usr/bin/python3
"""This class represents a class Rectangle"""


class Rectangle(BaseGeometry):
    '''A subclass of BaseGeometry'''

    def __init__(self, width, height):
        '''Initialising an instance'''

        self.integer_validator("width", width)
        selt.integer_validator("height", height)
        self.__width = width
        self.__height = height
