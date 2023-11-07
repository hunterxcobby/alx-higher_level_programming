#!/usr/bin/python3

"""
Module to write an Object into a text file using the JSON representation.
Prototype: def save_to_json_file(my_obj, filename):
You must use the with statement
You don’t need to manage exceptions if the object can’t be serialized.
You don’t need to manage file permission exceptions.
"""


def save_to_json_file(my_obj, filename):
    """
    define function to write Object to textfile.
    Args:
        my_obj: object to write
        filename: textfile to be written into

    """
    import json

    with open(filename, 'w') as my_file:
        new_files = my_file.write(json.dumps(my_obj))
        return new_files
