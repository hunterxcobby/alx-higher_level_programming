#!/bin/bash
# Bash script that take in a URL, sends a request to it, and displays the size of the body of the response, size should be displayed in bytes
curl -s "$1" | wc -c
