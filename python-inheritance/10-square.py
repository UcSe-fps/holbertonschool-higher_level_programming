#!/usr/bin/python3

""""new way"""
Rectangle = __import__(9-rectangle.py).Rectangle

"""new class"""

class Square(Rectangle):
    def __init__(self, size):
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(self.__size, self.__size)
    
    """new def"""

    def area(self):
         """returns soze"""
        
        return self.__size * self.__size
