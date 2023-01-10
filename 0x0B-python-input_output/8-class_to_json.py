#!/usr/bin/python3
''' define module class_to_json '''


def class_to_json(obj):
    ''' return the dictionary description with simple data structure
    Args:
        obj: class instance to be converted to json
    '''
    return obj.__dict__
