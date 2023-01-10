#!/usr/bin/python3
''' define a text file insertion function '''


def append_after(filename="", search_string="", new_string=""):
    ''' insert text after each line containing a given string in a file
    Args:
        filename (str): The name of the file
        search_string (str): The string to search for within the file
        new_string (str): The string to insert
    '''
    text = ""
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string

    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
