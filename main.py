#!/usr/bin/env python3

"""
Description: This module monitors websites checking live or down,
and also satisfying requirements or not.

Author: Alican Donmez - alicandonmez90@gmail.com.
"""

import logging
import csv
import sys
from helpers import monitor_site

logging.basicConfig(level=logging.DEBUG)


def main(*args, **kwargs):

    logging.info('Program started successfully')

    with open('config.csv', newline='') as handle_read:
        reader = csv.reader(handle_read)
        rownum = 0
        handle_write = open('log.csv', 'w')
        writer = csv.writer(handle_write)
        writer.writerow(('NAME', 'LIVE', 'SATISFY', 'ELAPSED TIME'))

        for row in reader:
            if rownum != 0:
                live, satisfy, elapsed_time = monitor_site(row[1], row[2])
                writer.writerow((row[0], live, satisfy, elapsed_time))

            rownum += 1
        handle_write.close()


if __name__ == '__main__':
    main()
