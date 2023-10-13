#!/usr/bin/python3

def common_elements(set_1, set_2):
    commonWords = set()
    for words in set_1:
        if words in set_2:
            commonWords.add(words)
    return commonWords

# alternative...this short ways are killing me🤯😂:
# def common_elements(set_1, set_2):
# return set_1 & set_2
