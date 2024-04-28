#!/usr/bin/python3
"""
Retrieve and display the IDs of the 10 most recent commits (from the newest to the oldest) made by the user 'rails' in the 'rails' repository. Utilize the GitHub API for this task.
"""


if __name__ == '__main__':
    from requests import get
    from sys import argv

    repo = argv[1]
    owner = argv[2]
    i = 0

    URL = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)

    response = get(URL)
    json = response.json()

    for element in json:
        if i > 9:
            break
        sha = element.get('sha')
        author = element.get('commit').get('author').get('name')
        print("{}: {}".format(sha, author))
        i += 1
