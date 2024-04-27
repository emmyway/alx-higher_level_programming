#!/bin/bash
# script sends a json POST to a url
curl -s -H "Content-Type: application/json" -d @"$2" "$1"
