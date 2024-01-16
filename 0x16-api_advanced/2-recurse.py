#!/usr/bin/python3
""" Recursive hot topics """
import requests


def recurse(subreddit, hot_list=[], after=""):
    """ fetch 10 hot topics from reddit """
    res = requests.get(
            "https://www.reddit.com/r/{}/hot.json".format(subreddit),
            headers={"User-Agent": "Custom"},
            params={"after":after},
    )
    if res.status_code == 200:
        for data in res.json().get("data").get("children"):
            title = data.get("data").get("title")
            hot_list.append(title)
        after = res.json().get("data").get("after")
        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None
