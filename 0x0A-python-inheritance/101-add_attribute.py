#!/usr/bin/python3

"""
Module to add new attributes to objects,
if it's possible.
Raise exceptions if the object cannot have new attribute.
Do not use try/except.
"""


def add_attribute(obj, attr, value):
    """
    Funtion that adds attribute if possible
    Args:
       obj
       name
       value
    Return: error if not possible
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
