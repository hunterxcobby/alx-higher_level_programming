#!/usr/bin/python3

""" Module to return the dictionary description with simple data structure
(list, dictionary, string, integer and boolean)
for JSON serialization of an object:
Prototype: def class_to_json(obj):
obj is an instance of a Class
All attributes of the obj Class are serializable:
list, dictionary, string, integer and boolean
You are not allowed to import any module
"""


def class_to_json(obj):
    """
    Class to json object
    Return:
        The dict for JSON serialization of an object
    """
    return obj.__dict__
