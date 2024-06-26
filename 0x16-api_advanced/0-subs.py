#!/usr/bin/python3
""" a function that queries the Reddit API and
returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """ a function that queries the Reddit API and
    returns the number of subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about/.json"
    headers = {
            "User-Agent": "Custem_Agent"
            }
    res = requests.get(url, headers=headers, allow_redirects=False)
    print(res)
    if res.status_code >= 300:
        return 0
    tmp = res.json()
    return tmp.get("data", {}).get("subscribers", 0)
