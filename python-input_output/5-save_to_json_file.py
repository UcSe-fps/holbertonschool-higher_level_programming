#!/usr/bin/python3
"""ahahahhaahah"""
import json


def save_to_json_file(my_obj, filename):
    """this is file"""

    with open(filename, mode='w', encoding='utf-8') as f:
        return json.dump(my_obj, f)
