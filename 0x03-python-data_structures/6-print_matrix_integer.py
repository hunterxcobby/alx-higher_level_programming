#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    #  ensure the function doesn't raise any errors. So if it is empty
    if not matrix:
        return
    # iterate through each row and column of the matrix.
    for row in matrix:
        for num in row:
            # print each integer using str.format() to format the output
            print("{:d}".format(num), end=" ")
        print()
