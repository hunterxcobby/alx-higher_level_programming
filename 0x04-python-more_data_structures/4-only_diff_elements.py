#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    difference = set()
    for element in set_1:
        if element not in set_2:
            difference.add(element)
    for element in set_2:
        if element not in set_1:
            difference.add(element)
    return difference

# an alternative:
# def only_diff_elements(set_1, set_2):
# return set_1 ^ set_2
