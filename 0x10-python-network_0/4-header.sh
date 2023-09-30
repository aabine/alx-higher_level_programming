#!/bin/bash
# Define the URL and header variable
URL="$1"
HEADER="X-School-User-Id: 98"

# Send the GET request with the specified header using curl and display the response body
curl -s -H "$HEADER" "$URL"
