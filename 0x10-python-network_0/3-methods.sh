#!/bin/bash
# Retrieve and display the HTTP methods supported by the server for a given URL.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
