#!/usr/bin/python3
"""
Initiates a request to the specified URL and exhibits the X-Request-Id variable value found in the response header.
"""

if __name__ == '__main__':
    from requests import get
    from sys import argv

    res = get(argv[1])
    print(res.headers.get('X-Request-Id'))
