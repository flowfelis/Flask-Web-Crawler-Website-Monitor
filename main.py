#!/usr/bin/env python3

"""
Description: This module monitors websites checking live or down,
and also satisfying requirements or not.

Author: Alican Donmez - alicandonmez90@gmail.com.
"""

import logging
from helpers import monitor_site

logging.basicConfig(level=logging.DEBUG)


def main(*args, **kwargs):

    logging.info('Program started successfully')



if __name__ == '__main__':
    main()
