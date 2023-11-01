#!/usr/bin/python3

"""
Print Square module
The module prints a square using `#`
Prototype: def print_square(size):
size is the size length of the square
Raise exceptions if size is not an int, or if size is less than 0,
or if size is a float and also less than 0.
"""


def print_square(size):
    """
    Print a perfect sqaure, given a valid int argument.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    else:
        for x in range(size):
            print("#" * size)
