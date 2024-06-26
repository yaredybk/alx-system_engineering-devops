#!/usr/bin/python3
"""task-2 subreddit"""
import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """recursive function that queries the Reddit API and
    returns a list containing the titles of
    all hot articles for a given subreddit. If no results are found for
    the given subreddit, the function should return None."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "yared@alx-holbertonschool"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code >= 300:
        return None

    results = response.json().get("data", {})
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
