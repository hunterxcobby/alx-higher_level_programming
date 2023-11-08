#!/usr/bin/python3

"""
Pascal Triangle Module.
"""


def pascal_triangle(n):
    """
    Function to generate the Pascal Triangle up to the nth row
    Args:
        n (int): Number of rows to generate.
    Return:
        a list of lists of integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    triangle = []
    for i in range(n):
        row = [1]  # The first element in each row go be 1

        # Calculate the next elements in the row
        if i > 1:
            prev_row = triangle[i - 1]
            for j in range(1, i):
                new_element = prev_row[j - 1] + prev_row[j]
                row.append(new_element)

        # Append 1 to the end of each row
        if i > 0:
            row.append(1)

        triangle.append(row)

    return triangle
