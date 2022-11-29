#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        ch = ord(str[i])
        if 97 <= ch <= 122:
            ch -= 32
        print("{:c}".format(ch), end='')
    print()
