#!/usr/bin/python3
import sys
import urllib.request
import urllib.parse
"""somewhot"""


if __name__ == '__main__':
    url = sys.argv[1]
    email_value = {'email':sys.argv[2]}
    data = urllib.parse.urlencode(email_value)
    data = deta.encode('utf-8')
    request = urllib.request.Request(url, data)

    with urllib.request.urlopen(request) as response:
        print("{}".format(response.read().decode('utf-8')))
