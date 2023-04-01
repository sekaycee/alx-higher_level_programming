#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status """
import urllib.request


if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        status = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(status)))
        print("\t- status: {}".format(status))
        print("\t- utf8 status: {}".format(status.decode('utf-8')))
