#!/usr/bin/python3

import sys
import requests

# Get the username and access token from command line arguments
username = sys.argv[1]
access_token = sys.argv[2]

# Create a session object to make HTTP requests
session = requests.Session()

# Set the authentication credentials for the session
session.auth = (username, access_token)

try:
    # Send a GET request to the GitHub API to fetch user information
    response = session.get("https://api.github.com/user", timeout=10)
    response.raise_for_status()

    # Parse the response as JSON
    userInfo = response.json()
    userId = userInfo.get("id")

    if userId:
        print(userId)
    else:
        print(None)

except requests.exceptions.RequestException as e:
    # Print the exception message if an error occurs during the request
    print(f"Exception: {e}")
