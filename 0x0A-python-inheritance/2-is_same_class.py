#!/usr/bin/python3

"""
Is_same_class Module.
Compare and return if object is exactly an instance of the specified class.
"""


def is_same_class(obj, a_class):
    """
    Function that checks if the object
    is exactly an instance of a_class
    Args:
        obj: object
        a_class: class
    """
    if type(obj) is a_class:
        return True
    else:
        return False
