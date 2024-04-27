#!/bin/bash
# Dispatches a GET request to a specified URL and exhibits the response status code.
curl -s -o /dev/null -w "%{http_code}" "$1"
