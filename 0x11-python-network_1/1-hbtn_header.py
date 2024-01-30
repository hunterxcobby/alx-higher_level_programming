#!/usr/bin/python3
import urllib.request
import sys

"""Displays the X-Request-Id header variable of a request to a given URL.
Usage: ./1-hbtn_header.py <URL>
"""

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    header = response.info()
    print(header['X-Request-Id'])
