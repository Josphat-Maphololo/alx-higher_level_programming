#!/bin/bash
# Get request to the URL and display the body of the response
curl -sL -X PUT -H "origin" -D "user-id" -o - 0.0.0.0:5000/catch_me
