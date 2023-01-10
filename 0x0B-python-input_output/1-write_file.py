#!/usr/bin/python3
''' write a string to text file & return nō of chars written '''


def write_file(filename="", text=""):
    ''' write to a file
    Args:
        filename: filename
        text: text to write
    Raises
        Exception: when the file can't be opened
    '''
    with open(filename, 'w', encoding="utf-8") as f:
        return (f.write(text))
