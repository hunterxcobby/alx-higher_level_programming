#!/usr/bin/python3

"""
Lookup object Module.
Creates a function with the prototype lookup(obj).
"""


def lookup(obj):
    """
    Funcion that returns list of available attributes
    and methods of an object.
    """
    return dir(obj)
