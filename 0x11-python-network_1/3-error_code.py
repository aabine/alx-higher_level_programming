#!/usr/bin/python3
"""
A script that takes a URL from
the command line and displays the content
"""
import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    try:
        URL = sys.argv[1]
        with urllib.request.urlopen(URL) as response:
            result = response.read().decode("utf-8")
            print(result)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
