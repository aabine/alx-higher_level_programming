#!/usr/bin/python3
import requests
""" A script that gets respones code from https://intranet.hbtn.io/status """

try:
    URL = "https://intranet.hbtn.io/status"
    response = requests.get(URL, timeout=10)
    response.raise_for_status()

    if response.status_code >= 200 and response.status_code < 400:
        print("Body response:")
        print(f"\t- type: {type(response.headers['content-type'])}")
        print(f"\t- content: {response.text}")
    else:
        print(f"Unexpected status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Exception: {e}")
