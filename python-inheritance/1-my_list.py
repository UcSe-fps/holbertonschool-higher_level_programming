#!/usr/bin/python3
"""MyList class that inherits from list"""

class MyList(list):
    """Custom list class with print_sorted method"""
    
    def print_sorted(self):
        """Prints the list in ascending sorted order"""
        print(sorted(self))
