#!/usr/bin/python3
def uppercase(str):
    for c in str:
        k = ord(c)
        if (k >= ord('a')) and (k <= ord('z')):	 # or k -= 32 (ASCII)
            c = chr(k-ord('a')+ord('A'))
        print("{}".format(c), end='')
    print()
