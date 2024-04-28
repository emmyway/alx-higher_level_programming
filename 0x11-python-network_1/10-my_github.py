#!/usr/bin/python3
'''
script otakes your GitHub credentials (username and password)
and uses the GitHub API to display your id
'''
import requests
import sys

url = "https://api.github.com/user"

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    # send request
    response = requests.get(url, auth(username, password))
    
    # obtain json version of respond
    usr_data = response.json()

    # print id info
    print(usr_data["id"])
