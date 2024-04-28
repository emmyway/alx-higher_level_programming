#!/usr/bin/python3
'''
script
'''
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    response = requests.post(url, data=value)

    print(response.text)
