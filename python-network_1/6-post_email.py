#!/usr/bin/python3
"""comment ig"""
import requests
import sys


if __name__ == '__main__':
    para = {'email' : 'email')
    r = requests.get(sys.argv[1], para)
    print(r.text)
