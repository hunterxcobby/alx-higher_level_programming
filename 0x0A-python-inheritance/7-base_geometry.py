#!/usr/bin/python3

"""
Module for Base Geometry based on `6-base_geometry`
Public instance method: def area(self):
that raises an Exception with the message area() is not implemented
Public instance method: def integer_validator(self, name, value):
that validates value:
If value is not an integer: raise a TypeError exception,
with the message <name> must be an integer
if value is less or equal to 0: raise a ValueError exception
with the message <name> must be greater than 0
"""


class BaseGeometry:
    """
    A class that defines the geometry
    """
    def area(self):
        """
        unimplemented area function
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        integer validation
        Args
           name: name of value
           value: value
        Must be an int greater than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
