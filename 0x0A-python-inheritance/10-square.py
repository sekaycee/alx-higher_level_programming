#!/usr/bin/python3


''' create class Square that inherits from class Rectangle '''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    ''' define a Square from Rectangle class '''
    def __init__(self, size):
        ''' initializes a Square '''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        ''' return a string with the area '''
        return (super().area())
