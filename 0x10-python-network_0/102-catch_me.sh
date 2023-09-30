#!/bin/bash
# Sends a POST request to 0.0.0.0:5000/catch_me with specific headers and data to get the message "You got me!".

curl -sL -X POST -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
