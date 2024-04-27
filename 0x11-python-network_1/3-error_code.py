#!/usr/bin/python3
'''
script takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8).
'''
import urllib.request
import sys
import urllib.error

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        # send s the request
        with urllib.request.urlopen(url) as response:
            body = response.read().decode("utf-8")

        print(body)

        # catches error
    except urllib.error.HTTPError as e:
        print("Error code", e.code)
