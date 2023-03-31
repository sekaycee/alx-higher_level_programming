#!/usr/bin/python3
''' Display the X-Request-Id header variable of a request to a given URL '''
import requests
import sys


if __name__ == '__main__':
    req = requests.get(sys.argv[1])
    print(req.headers['X-Request-Id'])
