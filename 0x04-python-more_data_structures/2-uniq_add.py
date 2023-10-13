#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_set = set(my_list)  # use set to store unique integers
    add_result = sum(unique_set)  # sum them up
    return add_result

#  alternative:
# def uniq_add(my_list=[]):
# return sum(set(my_list))
