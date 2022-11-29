#!/usr/bin/python3
def remove_char_at(str, n):
    # this is the python way
    # if 0 <= n < len(str):
    #    return (str.replace(str[n], ""))
    # return (str)

    # the c in python way
    s = ""
    for i in range(len(str)):
        if i != n:
            s += str[i]
    return (s)
