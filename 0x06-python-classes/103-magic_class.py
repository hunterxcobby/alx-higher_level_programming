#!/usr/bin/python3

"""Define a MagicClass matching bytecode provided in Task 10"""

import math


class MagicClass:
    """
    Initialize and define methods area and circumference
    to represent a circle.
    """
    def __init__(self, radius=0):
        """
        Initialize a MagicClass.
        Arguments:
            radius of MagicClass. Must be float or int
        """
        self.__radius = 0

        #  verify that radius is a number
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        #  update attribute
        self.__radius = radius

    def area(self):
        """
        Returns the area of our MagicClass.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates and returns the circumference of our MagicClass.
        """
        return 2 * math.pi * self.__radius
