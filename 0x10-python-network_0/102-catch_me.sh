#!/bin/bash
# Get request to the URL and display the body of the response
curl -L -X PUT -H "origin" -D "user-id" 0.0.0.0:5000/catch_me
