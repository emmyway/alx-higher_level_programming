#!/usr/bin/python3
'''
script list 10 commits (from the most recent to oldest) of
the repository “rails” by the user “rails" using the GitHub API
'''
import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = f"https://developer.github.com/v3/repos/{repo_name}/{owner_name}/commits/"

    response = requests.get(url)
    usr_commit = response.json()
    
    for i in range(10):
        sha = usr_commit["sha"]
        author_name = usr_commit["commit"]["author"]["name"]
        print({sha}: {author_name})
