#!/usr/bin/bash
# script
curl -s -o /dev/null -w "%{http_code}" "$1"
