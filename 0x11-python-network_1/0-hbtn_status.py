#!/usr/bin/python3
import urllib.request

""" A script that fetches https://intranet.hbtn.io/status """

if __name__ == "__main__":

    URL = "https://intranet.hbtn.io/status"

    with urllib.request.urlopen(URL) as response:
        data = response.read()

    print("Body response:")
    print(f"\t- type: {type(data)}")
    print(f"\t- content: {data}")
    print(f"\t- utf8 content: {data.decode('utf8')}")
