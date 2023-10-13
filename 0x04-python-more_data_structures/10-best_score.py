#!/usr/bin/python3

def best_score(a_dictionary):
    best_key = None
    best_value = None

    if a_dictionary is not None and len(a_dictionary) > 0:
        for key, value in a_dictionary.items():
            if best_value is None or value > best_value:
                best_key = key
                best_value = value

    return best_key
