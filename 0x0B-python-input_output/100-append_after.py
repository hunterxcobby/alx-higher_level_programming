#!/usr/bin/python3

"""
Search and Update Module.
Will contain function that inserts a line of text to a file,
after each line containing a specific string
(see 100-main.py & append_after_100.py):
Prototype: def append_after(filename="", search_string="", new_string=""):
You must use the with statement
You don’t need to manage file permission or file doesn't exist exceptions.
You are not allowed to import any module
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text into a file after each line
    containing a specific string.

    Args:
        filename (str): The name of the file to modify.
        search_string (str): The string to search for in each line.
        new_string (str): The line of text to insert after lines
        that contain the search string.
    Return: Nothing.
    """
    with open(filename, 'r', encoding="UTF8") as my_file:
        lines = my_file.readlines()

    with open(filename, 'w', encoding="UTF8") as my_file:
        for line in lines:
            my_file.write(line)
            if search_string in line:
                my_file.write(new_string)
