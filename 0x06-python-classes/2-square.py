#!/usr/bin/python3

"""
Create class Square that defines a square by

Private instance attribute: size
"""


class Square:
    """
    Instantiating the variables self and size.
    Raising errors if conditions are not met.
    """
    def __init__(self, size=0):
        #  verify that size is an integer
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        #  verify that size is less than 0
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
