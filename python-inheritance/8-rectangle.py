#!/usr/bin/python3
"""again sm bs"""



BaseGeometry = __import__('7-base_geometry').BaseGeometry




"""once more"""

class Rectangle(BaseGeometry):


    def __init__(self, height, width):
        """authentic"""

        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
