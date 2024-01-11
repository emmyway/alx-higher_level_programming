#!/ust/bin/python3

import json


def load_from_json_file(filename):
    '''fxn creates an Object from a “JSON file”
    Args:
        filename (str): the file name
    '''
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
