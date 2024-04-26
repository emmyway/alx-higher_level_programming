#!/bin/bash
# script sends a request to a url and displys only the status code of the response
curl -s -o /dev/null -w "%{http_code}" "$1"
