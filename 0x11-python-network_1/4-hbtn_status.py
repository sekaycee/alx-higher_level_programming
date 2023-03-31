#!/usr/bin/python3
''' Python script that fetches an URL with requests package '''
import requests


if __name__ == '__main__':
    txt = requests.get('https://intranet.hbtn.io/status').text
    print(f'Body response:\n\t- type: {type(txt)}\n\t- content: {txt}')
