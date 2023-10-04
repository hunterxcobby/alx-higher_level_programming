#!/usr/bin/python3

# to see byte code, uncomment next two lines and running ./<filename>
# import dis
# print(dis.dis(magic_calculation))

def magic_calculation(a, b, c):
    if a < b:
        return c
    elif c > b:
        return a + b
    else:
        return (a * b) - c
