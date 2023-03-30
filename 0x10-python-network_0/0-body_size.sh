#!/bin/bash
# Get the size in bytes of the HTTP response body for a given URL
curl -s "$1" | wc -c
