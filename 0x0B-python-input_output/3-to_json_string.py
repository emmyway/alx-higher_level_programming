#!/usr/bin/python3

import json


def to_json_string(my_obj):
    '''fxn returns json string of objects
    Args:
        my_obj (obj): the python object
    Return:
        json stri g representation
    '''
    return json.dumps(my_obj)
