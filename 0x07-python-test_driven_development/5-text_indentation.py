#!/usr/bin/python3
"""
Define function that indents text
"""


def text_indentation(text):
    """ print 2 new lines after ".?:" characters
    Args:
        text: input string
    Raises:
        TypeError: If text is not a string
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    s = text[:]
    for d in ".?:":
        list_t = s.split(d)
        s = ""
        for i in list_t:
            i = i.strip(" ")
            s = i + d if s is "" else s + "\n\n" + i + d

    print(s[:-3], end='')
