#!/usr/bin/python3
"""File containing top ten function"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    if response.status_code == 200:
        hot_posts = response.json().get('data').get('children')
        for post in hot_posts:
            print(post.get('data').get('title'))
    else:
        print(None)
