#!/usr/bin/python3

"""Python script that takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id in the response header.
Usage: ./5-hbtn_header.py <URL>
"""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    request_id = response.headers.get('X-Request-Id')

    print(request_id)
