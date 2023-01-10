#!/usr/bin/python3
''' define function that reads from a file '''


def read_file(filename=""):
    ''' read from a file
    Args:
        filename: filename
    Raises
        Exception: when the file can be opened
    '''
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end='')
