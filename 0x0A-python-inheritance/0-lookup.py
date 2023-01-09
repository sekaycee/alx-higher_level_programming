#!/usr/bin/python3
''' return list of object attributes '''


def lookup(obj):
    ''' return the list of available attributes
        and methods of an object
    Args:
        obj: instance of the class
    Returns:
        List of attributes
    '''
    return dir(obj)
