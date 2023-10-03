#!/usr/bin/python3
import sys
import requests

if __name__ == "__main__":
    try:
        # Get the URL and email from command-line arguments
        URL = sys.argv[1]
        response = requests.get(URL, timeout=10)
        response.raise_for_status()

        if response.status_code >= 200 and response.status_code < 400:
            print("Body response:")
            print(f"\t- type: {type(response.headers['content-type'])}")
            print(f"\t- content: {response.text}")
        else:
            print(f"Error code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Exception: {e}")
