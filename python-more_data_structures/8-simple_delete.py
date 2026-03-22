#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    new_set = []
    for i in a_dictionary:
        if i == key:
            del i
        else:
            return a_dictionary
