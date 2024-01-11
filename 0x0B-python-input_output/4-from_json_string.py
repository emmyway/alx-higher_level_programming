#!/usr/bin/python3

import json


def from_json_string(my_str):
    '''return python object representation of json string
    Args:
        my_str (json str): the json string given
    Return:
        python object
    '''
    return json.loads(my_str)
