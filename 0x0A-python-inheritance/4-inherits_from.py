#!/usr/bin/python3
''' check if an object is an inherited instance '''


def inherits_from(obj, a_class):
    ''' return True/False if obj is an instance of a_class
    Args:
        obj: object
        a_class: class type
    Returns:
        True if obj is an instance of a_class
        False, otherwise
    '''
    return (type(obj) != a_class and isinstance(obj, a_class))
