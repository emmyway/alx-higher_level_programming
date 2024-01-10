#!/usr/bin/python3

def read_file(filename=""):
    '''fxn reads a file objevt and print to stdout
    Args: 
        filename (ob): the file obj parameter
    '''

    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read())
