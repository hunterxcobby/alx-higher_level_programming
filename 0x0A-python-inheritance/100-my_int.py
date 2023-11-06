#!/usr/bin/python3

"""
Module MyInt
Inherit from int
MyInt is a rebel. MyInt has == and != operators inverted
"""


class MyInt(int):
    """
    class utilizing int class that will
    define a class that inverts == !=. operators
    """

    def __eq__(self, other):
        """initializer for eq"""
        if int.__ne__(self, other):
            return True
        else:
            return False

    def __ne__(self, other):
        """intializer for greater than"""
        if int.__eq__(self, other):
            return True
        else:
            return False
