#!/usr/bin/python3

"""
Text Indentation module
This module adds two new lines after these characters: ".?:"
and doesn't print any spaces at the beginning or end
of the given sentence.
Prototype: def text_indentation(text):
Raise exceptions if text is not a string.
"""


def text_indentation(text):
    """
    Function that prints 2 new lines after these chars:
    ".", "?" and ":"
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # initialize variable to hold final string
    final_str = ""

    # flag to skip/trim leading whitespaces
    trim_spaces = True

    # iterate through all chars in the given text
    for char in text:
        # check if char is one of these: '.', '?' or ':'
        if char in ".?:":
            final_str += char + "\n\n"  # add char and two new lines
            trim_spaces = True  # set flag to skip leading whitespaces
        elif char != " " or not trim_spaces:
            final_str += char
            trim_spaces = False  # reset flag if it's a non-space character

    print(final_str)
