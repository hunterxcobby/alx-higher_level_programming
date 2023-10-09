#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    # ensure the function doesn't raise any errors if list is empty
    if not my_list:
        return
    # loop through the elements of my_list in reverse order
    for i in range(len(my_list) - 1, -1, -1):
        # loop through the elements of my_list in reverse order
        print("{:d}".format(my_list[i]))
