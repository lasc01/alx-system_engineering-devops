#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""
import requests

def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 100, "after": after} if after else {"limit": 100}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()["data"]
        after = data["after"]
        children = data["children"]

        for child in children:
            title = child["data"]["title"]
            hot_list.append(title)

        if after:
            recurse(subreddit, hot_list, after)

    elif response.status_code == 404:
        return None

    return hot_list

