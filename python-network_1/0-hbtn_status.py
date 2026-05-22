#!/usr/bin/python3
"""importing"""
import urrllib.request
"""now comes the main part"""


with urllib.request.urlopen(https://intranet.hbtn.io/status) as f:
    html = f.read()
    """now printings"""
    
    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
    print("\t- utf8 content:", body.decode("utf-8"))
