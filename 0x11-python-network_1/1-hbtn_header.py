#!/usr/bin/python3
'''
Python script that takes in a URL, sends a request and displays
the value of the X-Request-Id variable found in the header
'''
from urllib import request
import sys


if __name__ == '__main__':
    with request.urlopen(sys.argv[1]) as res:
        print(res.info().get('X-Request-Id'))
