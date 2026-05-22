#!/usr/bin/python3
import requests
import sys

q = sys.argv[1] if len(sys.argv) > 1 else ""

r = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})

try:
    data = r.json()
    if data:
        print("[{}] {}".format(data["id"], data["name"]))
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
