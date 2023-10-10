#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    length1 = len(tuple_a)
    length2 = len(tuple_b)
    if length1 < 2:
        tuple_a += (0, 0)
    if length2 < 2:
        tuple_b += (0, 0)

    new_tuple = tuple_a[0]+tuple_b[0], tuple_a[1]+tuple_b[1]
    return new_tuple
