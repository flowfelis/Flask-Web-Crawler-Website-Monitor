"""This module contains helper functions"""

import requests


def monitor_site(url, req):
    """
    checks if site is live and satisfies requirements.

    Positional arguments:
    url -- the url of the website
    req -- the requirement string to check if exist on response

    Returns a tuple which confirms:
    first element of tuple  -- website live?
    second element of tuple -- requirement satisfied?
    third element of tuple  -- elapsed second while fetching
    """
    response = requests.request('get', url)
    return str(response.ok), str(False if response.text.find(req) == -1 else True), response.elapsed.total_seconds()
