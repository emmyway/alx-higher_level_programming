#!/usr/bin/python3
'''
script takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
'''
import requests
import sys

if __name__ == "__main__":
    # validate argument
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    q = letter
    url = "http://0.0.0.0:5000/search_user"
    data = {"q": q}
    try:
        # send POST request
        response = requests.post(url, data = data)
        json_data = response.json()

        # validate and print json data
        if json_data:
            print(f"[{json_data["id"]}] {json_data["name"]}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
