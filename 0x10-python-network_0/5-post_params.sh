#!/bin/bash
# script summits info to a url using POST method
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
