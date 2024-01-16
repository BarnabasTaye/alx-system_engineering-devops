#!/usr/bin/python3
""" Fetch top 10 hot posts listed """
import requests


def top_ten(subreddit):
    """ fetch the top 10 topics """
    res = requests.get(
            "https://www.reddit.com/r/{}/hot.json".format(subreddit),
            headers={"User-Agent": "Custom"},
            params={"limit": 10},
    )
    if res.status_code == 200:
        for data in res.json().get("data").get("children"):
            posts_title = data.get("data").get("title")
            print(posts_title)
    else:
        print(None)
