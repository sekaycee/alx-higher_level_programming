#!/usr/bin/python3
def add_attribute(obj, attr, value):
    ''' add a new attribute to an object
    Args:
        obj: object
        name: attribute name
        value: attribute value
    Raises:
        TypeError: when the attribute can't be added
    '''
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
