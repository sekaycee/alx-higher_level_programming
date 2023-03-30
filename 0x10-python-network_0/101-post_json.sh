#!/bin/bash
# Send a JSON POST request to a given URL and show the response body
curl -sH "Content-Type: application/json" -d "@$2" "$1"
