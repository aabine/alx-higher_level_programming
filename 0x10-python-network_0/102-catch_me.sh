#!/bin/bash
# Send a POST request to 0.0.0.0:5000/catch_me with a custom header
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
