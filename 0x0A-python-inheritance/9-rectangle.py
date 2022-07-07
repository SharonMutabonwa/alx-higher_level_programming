#!/usr/bin/python3
"""This module represents a subclass Rectangle"""

BaseGeometry = __import__('7-base_geometry.py').BaseGeometry


class Rectangle(BaseGeometry):
    '''This class inherits from BaseGeometry'''

    def __init__(self, width, height):
        '''Initializing an instance'''

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.width = width
        self.height = height

        def area(self):
            '''Implementing the area method'''

            return self.__width * self.__height

        def __str__(self):
            '''Returns a rectangle description: [Rectangle] <width>/<height>'''

            return "[Rectangle] {}/{}".format(self.__width, self.__height)
