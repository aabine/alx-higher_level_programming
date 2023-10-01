#!/usr/bin/python3
""" A script takes an email and sends a POST request to a specific URL """
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    URL, email = sys.argv[1], sys.argv[2]

    data = urllib.parse.urlencode({"email": email}).encode("ascii")

    req = urllib.request.Request(URL, data)

    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
