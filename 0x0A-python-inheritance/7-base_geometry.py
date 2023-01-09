#!/usr/bin/python3
''' define class BaseGeometry '''


class BaseGeometry:
    ''' define the attributes of Geometric Shapes '''
    def area(self):
        ''' define the area of a geomtric shape '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        ''' recieve the value property
        Árgs:
            name: name of the object
            value: value of the property
        '''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
