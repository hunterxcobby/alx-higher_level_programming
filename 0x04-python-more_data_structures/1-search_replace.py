#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = []
    for x in my_list:
        if x == search:
            new_list.append(replace)  # append replacement value
        else:
            new_list.append(x)  # append original

    return new_list

# the list comprehension way:
# def search_replace(my_list, search, replace):
# return [replace if search == x else x for x in my_list]
