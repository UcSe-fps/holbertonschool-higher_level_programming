#!/usr/bin/python3
"""last task"""
import sys
import requests


if __name__ == '__main__':
    url = ("https://api.github.com/user")
    username = sys.argv[1]
    password = sys.argv[2]
    infro = (username, password)
    r = requests.get(url, auth=info)
    try:
        print(r.json()['id'])
    except Exception:
        print('None')
