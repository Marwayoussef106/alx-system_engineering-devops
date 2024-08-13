#!/usr/bin/python3
"""use reddit api to print the number returns a
list containing the titles of all hot articles for a given subreddi"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """Reddit API endpoint for hot posts in a subreddit"""
    if hot_list is None:
        hot_list = []
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'
    if after:
        url += f'&after={after}'
    headers = {'User-Agent': 'your_user_agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            for post in data['data']['children']:
                title = post['data']['title']
                hot_list.append(title)
            # Recursive call with the 'after' parameter for pagination
            if 'after' in data['data'] and data['data']['after']:
                recurse(subreddit, hot_list, after=data['data']['after'])
            else:
                return hot_list
        else:
            return None
    elif response.status_code == 404:
        return None
    else:
        return None
