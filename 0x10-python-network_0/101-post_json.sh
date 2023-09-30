#!/bin/bash
# Sends a JSON POST request to the specified URL with the JSON content from a given file.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
