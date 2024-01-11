#!/usr/bin/python3

def append_write(filename="", text=""):
    '''fxn appends a string to file,
        create the file if not exist.
    Args:
        fileneame (str): the given file name
        text (str): the string to be written
    Return (int): the number of characters written
    '''
    with open(filename, 'a', encoding="utf-8") as f:
        num = f.write(text)
        return num
