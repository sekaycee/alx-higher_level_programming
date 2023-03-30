#!/bin/bash
# Make a request to 0.0.0.0:5000/catch_me to cause a response 'You got me!'
curl -sLX PUT 0.0.0.0:5000/catch_me -H "Origin:HolbertonSchool"
