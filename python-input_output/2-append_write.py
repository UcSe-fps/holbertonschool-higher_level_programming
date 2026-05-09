#!/usr/bin/python3
"""this is it"""

def append_write(filename="", text=""):
    """right back at you!"""

    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
