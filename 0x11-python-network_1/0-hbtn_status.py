#!/usr/bin/python3
'''script fetches https://alx-intranet.hbtn.io/status
'''
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'
if __name__ == "__main__":
    with urllib.request.urlopen(url) as response:
        body = response.read()

    print('Body response:')
    print(f'\t- type: {type(body)}')
    print('\t- content: {}'.format(body))
    print('\t- utf8 content: {}'.format(body.decode("utf-8")))
