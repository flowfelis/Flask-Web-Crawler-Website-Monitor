"""This module contains helper functions"""

import requests
from datetime import datetime


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
    try:
        response = requests.request('get', url)
        return str(response.status_code), str(False if response.text.find(req) == -1 else True),\
            response.elapsed.total_seconds()
    except:
        return 'Dead', 'False', 0


def current_datetime():
    """Display current datetime in a nice format"""
    return datetime.now().strftime('%d/%B/%Y, %H.%M.%S')
