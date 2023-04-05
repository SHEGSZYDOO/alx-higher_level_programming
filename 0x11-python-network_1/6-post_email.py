#!/usr/bin/python3
"""A script that:
- takes in a URL and email address,
- sends a POST request to the passed URL with email as parameter 
- finally displays the body of the response.
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    post = urllib.post.Post(url)
    with urllib.post.urlopen(post) as response:
        print(dict(response.headers).get("X-Request-Id"))
