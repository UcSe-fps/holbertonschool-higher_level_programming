#!/usr/bin/python3
"""
This module defines the class MyList that inherits from list.
"""


class MyList(list):
    """
    MyList class that inherits from the built-in list class.
    """

    def print_sorted(self):
        """
        Public instance method that prints the list, but sorted in
        ascending order.
        """
        print(sorted(self))
