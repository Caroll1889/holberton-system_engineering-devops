#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number
of subscribers for a given subreddit.
"""

import json
import requests


def number_of_subscribers(subreddit):

    url = 'https://api.reddit.com/r/{}/about'.format(subreddit)

    headers = {
        'User-Agent': 'My User Agent 1.0'
    }

    req = requests.get(url, headers=headers)

    if req.status_code == 200:

        req_json = req.json()

        data = req_json.get('data')
        sub = data.get('subscribers')
        return sub
    else:
        return 0
