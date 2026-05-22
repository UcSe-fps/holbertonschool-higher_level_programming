#!/usr/bin/python3
"""this will do it"""
import sys
import urllib.request


if __name__ == '__main__':
    request = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(request) as response:
            response.read().decode('utf-8')
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
