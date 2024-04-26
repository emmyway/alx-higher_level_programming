#!/bin/bash
# script takes in a url and display all http methods the server will accept
curl -sX OPTIONS -I "$1" | grep "Allow" | cut -d" " -f2-
