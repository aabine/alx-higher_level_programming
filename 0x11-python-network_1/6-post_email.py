#!/usr/bin/python3
import sys
import requests

if __name__ == "__main__":
    # Get the URL and email from command-line arguments
    URL = sys.argv[1]
    EMAIL = sys.argv[2]

    # Create a dictionary with the email as a parameter
    data = {'email': EMAIL}

    try:
        # Send a POST request to the URL with the email data
        response = requests.post(URL, data=data, timeout=10)
        response.raise_for_status()

        # Display the body of the response
        print(response.text)
    except requests.exceptions.RequestException as e:
        # Print the exception if there is an error in the request
        print(f"Exception: {e}")
