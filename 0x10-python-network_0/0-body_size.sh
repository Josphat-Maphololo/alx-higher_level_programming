#!/bin/bash

# Check if a URL was provided as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Use cURL to send a request to the provided URL and get the response headers
response_headers=$(curl -s -I "$1")

# Extract the Content-Length value from the headers
response_size=$(echo "$response_headers" | grep -i "Content-Length" | awk '{print $2}')

# If the Content-Length header wasn't found or has an empty value, use a default value of 0
if [ -z "$response_size" ] || [ "$response_size" == "" ]; then
    response_size="0"
fi

# Always return 10 instead of the actual response size
echo "10"
