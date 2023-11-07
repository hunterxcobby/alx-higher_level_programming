#!/usr/bin/python3

"""
Write a string into text file (UTF8) and return number of characters written.
Prototype: def write_file(filename="", text=""):
You must use the with statement
You don’t need to manage file permission exceptions.
Your function should create the file if doesn’t exist.
Your function should overwrite the content of the file if it already exists.
You are not allowed to import any module
"""


def write_file(filename="", text=""):
    """
    Write string into file and return number of characters written.
    Args:
        filename: file to write into
        text: content to write
    """
    with open(filename, 'w', encoding="UTF8") as myfile:
        content = myfile.write(text)
        return (content)
