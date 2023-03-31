#!/usr/bin/python3
'''
Python script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter, and
displays the body of the response
'''
from urllib import request, parse
import sys


if __name__ == '__main__':
    val = {'email': sys.argv[2]}
    data = parse.urlencode(val).encode('ascii')
    req = request.Request(sys.argv[1], data)
    with request.urlopen(req) as res:
        print(res.read().decode('utf-8'))
