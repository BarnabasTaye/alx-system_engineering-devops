#!/usr/bin/python3
""" Fetch the Reddit API number of subscribers """
import requests


def number_of_subscribers(subreddit):
    """ fetching the api """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "curl/7.81.0"}
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 404:
        return 0
    subs = res.json().get("data", {})
    return subs.get("subscribers")
