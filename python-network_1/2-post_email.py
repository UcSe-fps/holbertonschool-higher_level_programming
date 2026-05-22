#!/usr/bin/python3
"""lets see"""
import sys
import urllib.request
import urllib.parse


if __name__ == '__main__':
    url = sys.argv[1]
    email_value = {'email':sys.argv[2]}
    data = urllib.parse.urlenvode(email_value)
    request = urllib.request.Request(url, data)

    with urllib.request.urlopen(request) as response:
        print({}.format(response.read().decode('utf-8)))
