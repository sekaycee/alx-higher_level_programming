#!/usr/bin/python3
''' define function that returns the JSON repr of an object '''
import json


def to_json_string(my_obj):
    ''' return the JSON representation of an object
    Args:
        my_obj: object
    Raises:
        Exception: when the object can't be encoded
    '''
    return (json.dumps(my_obj))
