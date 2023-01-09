#!/usr/bin/python3
''' implememt class Rectangle that inherits the BaseGeometry class '''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' define a rectangle from BaseGeometry Class '''

    def __init__(self, width, height):
        ''' initialize instance '''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
