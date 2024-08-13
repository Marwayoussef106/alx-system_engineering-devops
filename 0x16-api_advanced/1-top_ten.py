#!/usr/bin/python3
"""use reddit api to print the number the titles of
the first 10 hot posts listed for a given subreddit."""
import requests


def top_ten(subreddit):
    """Reddit API endpoint for subreddit information"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'your_user_agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            for idx, post in enumerate(data['data']['children'][:10], start=1):
                title = post['data']['title']
                print(f"{idx}. {title}")
    elif response.status_code == 404:
        print("None")
