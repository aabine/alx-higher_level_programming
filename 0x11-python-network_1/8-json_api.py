#!/usr/bin/python3
import sys
import requests

if __name__ == "__main__":
    try:
        Url = "http://0.0.0.0:5000/search_user"
        letter = sys.argv[1] if len(sys.argv) > 1 else ""
        params = {"q": letter}

        response = requests.post(Url, params=params, timeout=10)
        response_json = response.json()

        if response.status_code == 200 and response_json:
            print(f"[{response_json['id']}] {response_json['name']}")
        elif not response_json:
            print("No result")
        else:
            print("Not a valid JSON")
    except requests.exceptions.RequestException as e:
        print(f"Exception: {e}")
