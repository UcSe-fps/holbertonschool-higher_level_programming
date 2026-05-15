#!/usr/bin/python3
"""this is it"""
import json


def serialize_and_save_to_file(data, filename):
    """
    
    this is another



    """

    with open(filename, 'w', encoding='utf-8') as f:
         json.dump(data, f)


def load_and_deserialize(filename):
    """

    this is too


    """




    with open(filename, 'w', encoding='utf-8') as f:
        return json.load(f)
