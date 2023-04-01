#!/usr/bin/python3
''' Python script that fetches an URL with requests package '''
import requests


if __name__ == '__main__':
    txt = requests.get('https://intranet.hbtn.io/status').text
    print('Body response:')
    print('\t- type: {}'.format(type(txt)))
    print('\t- content: {}'.format(txt))
