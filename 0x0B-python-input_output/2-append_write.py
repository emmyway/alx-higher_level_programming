#!/usr/bin/python3

def write_file(filename="", text=""):
    '''fxn writes a string to file
        create the file if not exist.
    Args:
        fileneame (obj): the given file
        text (string): the string to be written
    Return:
        the number of characters written
    '''
    with open(filename, 'w', encoding="utf-8") as f:
        num = f.write(text)
        return num
