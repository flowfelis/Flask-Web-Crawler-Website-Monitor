#!/usr/bin/env python3

"""
Description: This module monitors websites checking live or down,
and also satisfying requirements or not.

Author: Alican Donmez - alicandonmez90@gmail.com.
"""

import logging
import csv
import sys
import time
from helpers import monitor_site, current_datetime

logging.basicConfig(level=logging.INFO)


def main(*args, **kwargs):

    # limit command line arguments to 2
    if len(sys.argv) > 3:
        print('''
        Usage: main.py arg1 arg2
        arg1 -- time interval in seconds. Default: 60 seconds
        arg2 -- configuration file in csv extention. Default: config.csv
        
        ''')
        sys.exit(1)
    # validate args
    else:
        try:
            interval = int(sys.argv[1])
        except IndexError:
            interval = 10
        except ValueError:
            print('interval must be an integer')
            sys.exit(1)

        try:
            file = sys.argv[2]
        except IndexError:
            file = 'config.csv'

    logging.info('Program started successfully')
    logging.info('\ninterval time --> {0}\nreading from --> {1}'.format(interval, file))

    while True:

        with open(file, newline='') as handle_read:
            reader = csv.reader(handle_read)
            rownum = 0
            handle_write = open('log.csv', 'w')
            writer = csv.writer(handle_write)
            logging.info('Write Starting at ' + current_datetime() + '...')
            writer.writerow(('TIME OF EXECUTION', current_datetime()))
            writer.writerow(('NAME', 'URL', 'STATUS CODE', 'SATISFIED?', 'STRING', 'ELAPSED TIME'))

            for row in reader:
                if rownum != 0: # escape header
                    logging.info('{} => '.format(row[0]) + str(monitor_site(row[1], row[2])))
                    live, satisfy, elapsed_time = monitor_site(row[1], row[2])
                    writer.writerow((row[0], row[1], live, satisfy, row[2], elapsed_time))

                rownum += 1
            handle_write.close()
            logging.info('write completed. log.csv file is ready\n')
        time.sleep(interval)


if __name__ == '__main__':
    main()
