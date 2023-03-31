#!/usr/bin/python3
''' Python script that fetches https://intranet.hbtn.io/status '''


if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as res:
        status = res.read()
        print('Body response:')
        print('\t- type: {}'.format(type(status)))
        print('\t- content: {}'.format(status))
        print('\t- utf8 content: {}'.format(status.decode('utf-8')))
