#!/usr/bin/python3
"""Module that defines a MyList class inheriting from list"""

class MyList(list):
    """A custom list class that adds functionality to print a sorted version"""
    
    def print_sorted(self):
        """Prints the list in ascending sorted order without modifying the original list"""
        # Create a sorted copy and print it
        print(sorted(self))
