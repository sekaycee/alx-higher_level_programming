#!/usr/bin/python3
'''
Python script that sends a request to the URL and
displays:
- The body of the response if there are no errors
- The error code when there is an HTTP error.
'''
import requests
import sys


if __name__ == '__main__':
    req = requests.get(sys.argv[1])
    if req.status_code >= 400:
        print(f'Error code: {req.status_code}')
    else:
        print(req.text)
