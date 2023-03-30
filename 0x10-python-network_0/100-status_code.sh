#!/bin/bash
# Send a request to a URL, and show only the response status code
curl -so /dev/null -w "%{http_code}" "$1"
