#!/usr/bin/python3
"""comment ig"""
import requests
import sys


if __name__ == '__main__':
    para = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], data=para)
    print(r.text)
