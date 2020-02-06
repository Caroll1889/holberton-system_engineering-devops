#!/usr/bin/python3
"""
function that queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit.
"""

import json
import requests


def top_ten(subreddit):

    url = 'https://api.reddit.com/r/{}?sort=hot&limit=10'.format(subreddit)

    headers = {
        'User-Agent': 'My User Agent 1.0'
    }

    req = requests.get(url, headers=headers)

    if req.status_code == 200:
        req_json = req.json()

        data = req_json.get('data')
        children = data.get('children')
        for i in children:
            title = i.get('data').get('title')

            print(title)
    else:
        print(None)  
