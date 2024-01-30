#!/bin/bash
# Check if the number of arguments is not equal to 2
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <URL> <JSON_FILE>"
    exit 1
fi

# Check if the JSON file exists
if [ ! -f "$2" ]; then
    echo "JSON file '$2' does not exist."
    exit 1
fi

# Validate the JSON syntax
if ! jq . "$2" >/dev/null 2>&1; then
    echo "Not a valid JSON"
    exit 1
fi

# Send a JSON POST request to the URL with the contents of the JSON file
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
