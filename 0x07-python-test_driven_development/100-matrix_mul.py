#!/usr/bin/python3

"""
Matrix multiplication module.
Multiplies two matrices.
Must be list/ list of list
Raise exceptions where necessary.
"""


def matrix_mul(m_a, m_b):
    """
    Multiply matrices.

    Args:
        m_a: matrix a
        m_b: matrix b

    Return:
        Multiplication of a and b
    """

    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")

    err_msg1 = "m_a must be a list of lists or m_b must be a list of lists"
    if (
        not all(isinstance(row, list) for row in m_a)
        or not all(isinstance(row, list) for row in m_b)
    ):
        raise TypeError(err_msg1)

    if not m_a or not m_b:
        raise ValueError("m_a can't be empty or m_b can't be empty")

    if not all(isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

    # Perform matrix multiplication
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
