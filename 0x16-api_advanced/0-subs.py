#!/usr/bin/python3
"""use reddit api to print the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Reddit API endpoint for subreddit information"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'u/nourhan1414'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    data = response.json().get("data")
    subscribers = data.get('subscribers')
    return subscribers
