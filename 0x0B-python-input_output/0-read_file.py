#!/usr/bin/python3

"""
Using the UTF8 way, read a text file.
Print to stdout.
Prototype: def read_file(filename=""):
You must use the with statement
You don’t need to manage file permission or file doesn't exist exceptions.
"""


def read_file(filename=""):
    """
    Open and read a UTF8 file and print to stdout.
    Args:
        filename
    """
    with open(filename, encoding="UTF8") as myfile:
        text = myfile.read()
        print(text, end="")
