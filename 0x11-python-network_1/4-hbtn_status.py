#!/usr/bin/python3
'''
script fetches https://alx-intranet.hbtn.io/status using
request
'''
import requests

if __name__ == "__main__":
    url = https://alx-intranet.hbtn.io/status
    
    # send request
    response = requests.get(url)

    # display output
    print("Body response")
    print("\t- type:", type(response.text))
    print("\t- content:", respons4.text)
