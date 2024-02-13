#!/usr/bin/python3
""" queries the Reddit API and prints the titles of the first 10 hot posts
"""
import requests


def top_ten(subreddit):
    """ prints the titles of the first 10 hot posts
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    params = {"limit": 10}
    response = requests.get(url, params=params, allow_redirects=False)

    if response.status_code != 200:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
