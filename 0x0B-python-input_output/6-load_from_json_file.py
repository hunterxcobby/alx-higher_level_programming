#!/usr/bin/python3

"""
Module to create object from JSON file.
Prototype: def load_from_json_file(filename):
You must use the with statement
You do not need to manage exceptions if
the JSON string does not represent an object.
You do not need to manage file permissions / exceptions.
"""


def load_from_json_file(filename):
    """
    Function to load object from json file.
    Args:
        filename
    Return:
        object created from the file.
    """
    import json

    with open(filename) as obj_file:
        new_file = json.load(obj_file)
        return new_file
