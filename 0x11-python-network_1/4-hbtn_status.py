#!/usr/bin/python3
''' Python script that fetches an URL with requests package '''


if __name__ == '__main__':
    import requests

    t = requests.get('https://intranet.hbtn.io/status').text
    print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(t), t))
