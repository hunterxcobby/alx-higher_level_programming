#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    # handle the case where the index (idx) is negative
    # check if the index is greater than or equal to the number of elements
    if idx < 0 or idx >= len(my_list):
        return my_list
    # replace the element at that index in my_list.
    my_list[idx] = element
    return my_list
