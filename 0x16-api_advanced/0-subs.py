#!/usr/bin/python3
""" Queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """ return number of subscribers or 0 if invalid subredit
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, allow_redirects=False)

    if response.status_code == 200:
        results = response.json().get("data")
        return results.get("subscribers")
    return 0
