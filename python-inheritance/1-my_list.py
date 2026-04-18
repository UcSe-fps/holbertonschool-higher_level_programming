#!/usr/bin/python3
"""
This module defines the class MyList that inherits from the list class.
"""


class MyList(list):
    """
    MyList class that inherits from the list class.
    """

    def print_sorted(self):
        """
        Public instance method that prints the list, but sorted
        (ascending sort).
        """
        print(sorted(self))
