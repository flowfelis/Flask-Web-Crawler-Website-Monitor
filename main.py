#!/usr/bin/env python3

"""
Description: This module monitors websites checking live or down,
and also satisfying requirements or not.

Author: Alican Donmez - alicandonmez90@gmail.com.
"""

import requests
import logging

logging.basicConfig(level=logging.DEBUG)
logging.info('Program started successfully')

url = 'http://www.alida.com.tr'
req = 'Anasayfa'


def ok_and_match(url, req):
    response = requests.request('get', url)
    return response.ok, bool(response.text.find(req))
