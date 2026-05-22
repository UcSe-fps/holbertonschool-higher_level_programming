#!/usr/bin/python3
"""this will be smt"""
import requests

if __name__ == '__main__':
    html = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(html.text.__class__))
    print("\t- content: {}".format(html.text))
