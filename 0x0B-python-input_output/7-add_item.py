#!/usr/bin/python3

"""
Module to add all arguments to a Python list
and save them to a file.
You must use your function save_to_json_file from 5-save_to_json_file.py
You must use your function load_from_json_file from 6-load_from_json_file.py
The list must be saved as a JSON representation in a file named add_item.json
If the file doesn’t exist, it should be created
You don’t need to manage file permissions / exceptions.
"""


import json
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arg_check = len(sys.argv)  # to check number of cmd line args

try:
    # load exixting data from add-item.json
    my_list = load_from_json_file('add_item.json')
except FileNotFoundError:
    my_list = []  # initialize empty list if it doesn't exist

for x in range(1, arg_check):
    # append args to my_list
    my_list.append(sys.argv[x])
# update my_list with data from add-item.json
save_to_json_file(my_list, 'add_item.json')
