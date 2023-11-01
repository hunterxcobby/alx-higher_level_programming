# Setup: Import the module and function
>>> mod = __import__("100-matrix_mul")
>>> matrix_mul = mod.matrix_mul

# Function Documentation
>>> len(mod.__doc__) > 1
True

# Function Documentation
>>> len(matrix_mul.__doc__) > 1
True

# Test Cases

# Valid input: matrices that can be multiplied
>>> m_a = [[1, 2], [3, 4]]
>>> m_b = [[5, 6], [7, 8]]
>>> matrix_mul(m_a, m_b)
[[19, 22], [43, 50]]

# Valid input: matrices with floats
>>> m_a = [[1.0, 2.5], [3.5, 4.0]]
>>> m_b = [[5.0, 6.5], [7.5, 8.0]]
>>> matrix_mul(m_a, m_b)
[[23.75, 26.5], [47.5, 54.75]]

# Valid input: matrices with negative numbers
>>> m_a = [[-1, -2], [-3, -4]]
>>> m_b = [[5, 6], [7, 8]]
>>> matrix_mul(m_a, m_b)
[[-19, -22], [-43, -50]]

# Valid input: matrices with zeros
>>> m_a = [[0, 0], [0, 0]]
>>> m_b = [[5, 6], [7, 8]]
>>> matrix_mul(m_a, m_b)
[[0, 0], [0, 0]]

# Invalid input: m_a is not a list (invalid)
>>> m_a = "not_a_list"
>>> m_b = [[5, 6], [7, 8]]
>>> matrix_mul(m_a, m_b)
Traceback (most recent call last):
    ...
TypeError: m_a must be a list or m_b must be a list

# Invalid input: m_b is not a list (invalid)
>>> m_a = [[1, 2], [3, 4]]
>>> m_b = "not_a_list"
>>> matrix_mul(m_a, m_b)
Traceback (most recent call last):
    ...
TypeError: m_a must be a list or m_b must be a list

# Invalid input: m_a contains a non-number (invalid)
>>> m_a = [[1, 2], ["three", 4]]
>>> m_b = [[5, 6], [7, 8]]
>>> matrix_mul(m_a, m_b)
Traceback (most recent call last):
    ...
TypeError: m_a should contain only integers or floats

# Invalid input: m_b contains a non-number (invalid)
>>> m_a = [[1, 2], [3, 4]]
>>> m_b = [[5, 6], [7, "eight"]]
>>> matrix_mul(m_a, m_b)
Traceback (most recent call last):
    ...
TypeError: m_b should contain only integers or floats

# Invalid input: m_a is empty (invalid)
>>> m_a = []
>>> m_b = [[5, 6], [7, 8]]
>>> matrix_mul(m_a, m_b)
Traceback (most recent call last):
    ...
ValueError: m_a can't be empty or m_b can't be empty

# Invalid input: m_b is empty (invalid)
>>> m_a = [[1, 2], [3, 4]]
>>> m_b = []
>>> matrix_mul(m_a, m_b)
Traceback (most recent call last):
    ...
ValueError: m_a can't be empty or m_b can't be empty

# Invalid input: matrices with incompatible sizes (invalid)
>>> m_a = [[1, 2], [3, 4]]
>>> m_b = [[5, 6, 7], [8, 9, 10]]
>>> matrix_mul(m_a, m_b)
[[21, 24, 27], [47, 54, 61]]

# run test case file with `python3 -m doctest -v ./tests/100-matrix_mul.txt`
