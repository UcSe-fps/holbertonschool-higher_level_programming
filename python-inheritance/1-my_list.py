#!/usr/bin/python3
"""trying to make it"""


class MyList(list):
    def __init__(self):
        pass


    def print_sorted(self):
        """print the list sorted"""
        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))
