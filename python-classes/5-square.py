#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
"""class Square that defines a square"""
    def __init__(self, size):
        """Instantiation with optional size"""
        self.__size = size

    @property
    def size(self):
        """property setter to set it"""
        self.__size
    
    @size.setter
    def size(self, value):
        """property setter to set it"""
        if value is int:
            if value >= 0:
                value = self.__size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
    def area(self):
        """Public instance method that returns the current square area"""
        return self.__size * self.__size
