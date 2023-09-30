#!/bin/bash
# Check if a URL is provided as an argument
if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Define the URL and header variable
URL="$1"
HEADER="X-School-User-Id: 98"

# Send the GET request with the specified header using curl and display the response body
curl -s -H "$HEADER" "$URL"
