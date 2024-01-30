#!/bin/bash
# Send an OPTIONS request to the URL and display the Allow header
curl -sI "$1" | grep "Allow:" | cut -d ' ' -f2-
