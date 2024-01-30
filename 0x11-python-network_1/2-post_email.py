#!/usr/bin/python3
import urllib.parse
import urllib.request
import sys

url = sys.argv[1]
email = sys.argv[2]

data = urllib.parse.urlencode({'email': email})
data = data.encode('utf-8')

req = urllib.request.Request(url, data=data, method='POST')
with urllib.request.urlopen(req) as response:
    print(response.read().decode('utf-8'))
