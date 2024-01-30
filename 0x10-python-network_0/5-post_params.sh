#!/bin/bash
# Send a POST request to the URL with specified parameters and display the body of the response
curl -sX POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
