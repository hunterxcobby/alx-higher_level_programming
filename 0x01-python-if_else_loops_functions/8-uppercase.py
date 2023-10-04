#!/usr/bin/python3

def uppercase(s):
    for char in s:
        print("[{}].format(chr({}))".format(
            chr(ord(char) - 32) if 97 <= ord(char) <= 122 else char, ord(char)), end="")
    print()
