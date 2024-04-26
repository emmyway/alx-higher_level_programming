#!/bin/bash
# script gets a url and prints the size of the body
curl -s "$1" | wc -c
