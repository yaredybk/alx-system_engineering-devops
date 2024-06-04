#!/usr/bin/python3
"""
subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """ queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
            "User-Agent": "yared_alx"
            }
    params = {
            "limit": 10
            }
    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)
    if res.status_code >= 300:
        print(None)
        return
    tmp = res.json().get("data")
    [print(c.get("data").get("title")) for c in tmp.get("children")]
