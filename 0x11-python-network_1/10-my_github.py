#!/usr/bin/python3
'''
Python script that takes GitHub credentials
and uses the GitHub API to display the user id
'''
from requests import get, auth
import sys


if __name__ == '__main__':
    login = auth.HTTPBasicAuth(sys.argv[1], sys.argv[2])
    req = get('https://api.github.com/user', auth=login)
    print(req.json().get('id'))
