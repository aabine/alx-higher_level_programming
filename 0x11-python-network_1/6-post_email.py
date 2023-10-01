#!/usr/bin/python3
"""
A script that takes a URL and EMAIL from
The command line and displays the content 
"""

import sys
import requests
import requests.exceptions

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./0-hbtn_header.py <URL> <EMAIL>")
        sys.exit(1)
    data = {
        "URL": sys.argv[1],
        "EMAIL": sys.argv[2]
    }
    if not data["URL"].startswith("https://" or data["URL"].endswith("/")):
        data["URL"] = "https://" + data["URL"] + "/"
    try:
        response = requests.post(data["URL"], data=data, timeout=10)
        response.raise_for_status()
        with response:
            print(response.headers.get('X-Request-Id'))
    except requests.exceptions.RequestException as e:
        print(f"Exception: {e}")
