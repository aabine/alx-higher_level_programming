#!/usr/bin/python3

# Importing necessary modules
import sys
import requests

if __name__ == "__main__":
    # Retrieving repository name and owner from command line arguments
    repo_name = sys.argv[1]
    repo_owner = sys.argv[2]

    # Creating the URL for the GitHub API
    Url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits"
    try:
        # Sending a GET request to the GitHub API
        response = requests.get(Url, timeout=10)
        # Parsing the response as JSON
        result = response.json()
        # Printing the details of the last 10 commits
        for commit in result[:10]:
            sha = commit["sha"]
            author_name = commit["commit"]["author"]["name"]
            print(f"{sha}: {author_name}")
    except requests.exceptions.RequestException as e:
        print(f"Exception: {e}")
