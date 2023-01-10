#!/usr/bin/python3
''' write a string to text file & return nō of chars written '''


def write_file(filename="", text=""):
    ''' write to a file '''
    with open(filename, 'w') as f:
        return (f.write(text))
