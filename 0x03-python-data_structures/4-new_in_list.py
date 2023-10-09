#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    # handle the case where the index (idx) is negative or out of range
    if idx < 0 or idx >= len(my_list):
        # return a copy of the list
        return my_list[:]
    # create a copy of the original list.
    # This will ensure that we don't modify the original list
    new_list = my_list[:]
    # replace the element at that index
    new_list[idx] = element
    return new_list
