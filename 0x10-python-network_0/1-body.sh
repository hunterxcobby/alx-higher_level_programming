#!/bin/bash
# Bash script that takes a URL, sends a GET request to the URL
# and displays the body of the reponse, display only body of a 200 status code response
curl -sL "$1"