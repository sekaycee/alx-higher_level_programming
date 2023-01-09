#!/usr/bin/python3
def lookup(obj):
    ''' return the list of available attributes
        and methods of an object
    Args:
        obj: instance of the class
    Returns:
        List of attributes
    '''

    return dir(obj)
