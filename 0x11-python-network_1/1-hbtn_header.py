#!/usr/bin/python3
""" A script that recieves a URL and displays the value of the X-Request-Id """
import urllib.request
import sys

if __name__ == "__main__":
    # Retrieve the URL from the command line argument
    URL = sys.argv[1]

    # Open the URL and obtain a response object
    with urllib.request.urlopen(URL) as response:
        # Retrieve the headers as a list of tuples
        headers = response.getheaders()

        # Convert the headers into a dictionary
        headers_dict = dict(headers)

        # Print the value of the 'X-Request-Id' header
        print(headers_dict['X-Request-Id'])
