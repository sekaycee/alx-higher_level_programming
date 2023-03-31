#!/usr/bin/python3
'''
Python script that sends a POST request to the URL and
to an URL with the letter as a parameter
'''
import requests
import sys


if __name__ == '__main__':
    data = {'q': '' if len(sys.argv) == 1 else sys.argv[1]}
    req = requests.post('http://0.0.0.0:5000/search_user', data)
    try:
        obj = req.json()
        if not obj:
            print('No result')
        else:
            print(f'[{obj.get("id")}] {obj.get("name")}')
    except ValueError:
        print('Not a valid JSON')
