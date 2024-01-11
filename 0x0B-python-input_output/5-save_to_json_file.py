#!/usr/bin/python3

import json


def save_to_json_file(my_obj, filename):
    '''fxn wtites an object into a file, using json representation
    Args:
        my_obj (obj): the obj to be wtitten
        filename (str): the fike to be written to
    '''
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
