#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""
from urllib import request

if __name__ == "__main__":
    with request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
        html = resp.read()
        print('Body response:')
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
