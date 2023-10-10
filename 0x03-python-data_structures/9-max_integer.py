#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return None
    max_int = my_list[0]

    for i in my_list[1:]:
        if i > max_int:
            max_int = i
    return max_int
