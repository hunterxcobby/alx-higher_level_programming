#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    count = len(sys.argv) - 1  # Subtract 1 to exclude the script name
    if count == 0:  # check no of args and print accordingly
        print("{} arguments.".format('0'))
    elif count == 1:
        print("{} argument:".format(count))
    else:
        print("{} arguments:".format(count))

    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
