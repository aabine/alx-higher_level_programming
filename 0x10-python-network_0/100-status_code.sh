#!/bin/bash
# Sends a GET request to the URL, and displays the response status code( 200, 301, 400, etc..)
curl -s -o /dev/null -w "%{http_code}" "$1"
