#!/usr/bin/python3

"""
Matrix Division module
The module takes in a list of lists matrix and divisor.
Contains method that divides all the elements of a matrix
and returns new matrix
Requires same size lists of ints or floats, and max two decimal places
"""


def matrix_divided(matrix, div):
    """
    Return a new matrix with all values divided by `div`.
    Matrix must be a list of lists.
    Each sub-list must contain only integers or floats.
    Empty sub-lists are not allowed.
    Divisor must be greater than 0 and must be an int or float.
    """
    # variable to store the long error message due to pycodestyle warning
    matrixErrMsg = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix:
        raise TypeError(matrixErrMsg)
    elif type(matrix) is not list:
        raise TypeError(matrixErrMsg)
    elif len(matrix) == 0:
        raise TypeError(matrixErrMsg)
    elif len(matrix[0]) == 0:
        raise TypeError(matrixErrMsg)

    new_matrix = []
    matrix_len = len(matrix[0])

    for lists in matrix:
        if type(lists) is not list:
            raise TypeError(matrixErrMsg)
        if len(lists) != matrix_len:
            raise TypeError("Each row of the matrix must have the same size")

        newlist = []
        for x in lists:
            if not isinstance(x, (int, float)):
                raise TypeError(matrixErrMsg)
            newlist.append(round(x / div, 2))
        new_matrix.append(newlist)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif type(div) is bool:
        raise TypeError("div must be a number")
    elif type(div) is str:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return new_matrix
