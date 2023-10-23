#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True

    except (ValueError, TypeError) as error:
        # stderr.write("Exception: {}\n".format(error))
        print("Exception: {}".format(error), file=sys.stderr)
        return False
