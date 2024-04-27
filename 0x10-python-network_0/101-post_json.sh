#!/bin/bash
# Dispatches a JSON POST request to a specified URL along with a designated JSON file.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
