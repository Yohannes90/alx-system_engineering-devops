#!/usr/bin/python3
""" Queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """ return number of subscribers or 0 if invalid subredit
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code >= 300:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
