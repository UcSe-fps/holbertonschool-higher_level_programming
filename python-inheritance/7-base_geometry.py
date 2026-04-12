#!/usr/bin/python3
class BaseGeometry:
    """tihohv"""



    def area(self):
    """hfbvidbcin"""
        raise Exception("area() is not implemented")


"""third definition"""

    def integer_validator(self, name, value):
        """last part"""

        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        elif value <= 0:
            raise ValueError("<name> must be greater than 0")
