#!/usr/bin/python3
''' define a BaseGeometry class with method area unimplemented '''


class BaseGeometry:
    ''' Empty class '''
    def area(self):
        raise Exception("area() is not implemented")
