#!/usr/bin/python3

def lookup(obj):
    '''function returns the list of available attributes
    and methods of an object
    Args:
        obj (instance): the instance parameter
    Return: a list of available attributes and methods of an object
    '''
    return dir(obj)
