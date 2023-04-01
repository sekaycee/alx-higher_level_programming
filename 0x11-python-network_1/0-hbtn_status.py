#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status """


if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        status = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(status)))
        print("\t- status: {}".format(status))
        print("\t- utf8 status: {}".format(status.decode('utf-8')))
