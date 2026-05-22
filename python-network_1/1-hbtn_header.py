#!/usr/bin/python3
"""here is the coment"""
import sys
import urllib.request


if __name__ =+ '__main__':
    with urllib.request.urlopen(sys.argv[1]) as smt:
        print("{}".format(smt.getheader('X-Request-Id')))
