#!/usr/bin/python3
""" 
A script that receives a URL and 
displays the value of the X-Request-Id
"""
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-hbtn_header.py <URL>")
        sys.exit(1)

    URL = sys.argv[1]
    if not URL.startswith("https://" or URL.endswith("/")):
        URL = "https://" + URL + "/"

    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()
        with response:
            print(response.headers.get('X-Request-Id'))
    except requests.exceptions.RequestException as e:
        print(f"Exception: {e}")
