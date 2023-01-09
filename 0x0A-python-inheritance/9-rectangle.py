#!/usr/bin/python3


''' create class Rectangle that inherits BaseGeometry '''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' define a rectangle from BaseGeometry Class '''
    def __init__(self, width, height):
        ''' initialize instance '''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        ''' return the area of the instance '''
        return (self.__width * self.__height)

    def __str__(self):
        ''' return the printable string '''
        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))
