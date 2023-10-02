#!/usr/bin/python3

import sys

# write a message to standard error
sys.stderr.write("and that piece of art is useful - Dora Korpar, 2015-10-19\n")
# flush the buffer so it prints the text immediately
sys.stderr.flush()

# This indicates that the script terminated due to an error.
sys.exit(1)
