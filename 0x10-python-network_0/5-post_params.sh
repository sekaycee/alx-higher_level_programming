#!/bin/bash
# Get the response body from a POST request to a given URL
curl -sX "$1" POST -d "email=test@gmail.com&subject=I will always be here for PLD"
