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

# logging.basicConfig(level=logging.INFO)


def main():

    # complain if more than 2 arguments are given
    if len(sys.argv) > 3:
        print('''
        Usage: monitor.py <arg1> <arg2>
        arg1 -- time interval in seconds. Default: 10 seconds
        arg2 -- configuration file in csv extension. Default: config.csv
            Please note to create a header line if custom config file is given.
        
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
        with open(file) as handle_read:
            reader = csv.reader(handle_read)
            rownum = 0  # to escape header row
            handle_write = open('log.csv', 'a')  # for log.csv file
            handle_write_last = open('log_last.csv', 'w')  # for displaying last status on html
            writer = csv.writer(handle_write)
            writer_last = csv.writer(handle_write_last)
            logging.info('Write Starting at ' + current_datetime() + '...')
            writer.writerow(('TIME OF EXECUTION', current_datetime()))
            writer_last.writerow(('TIME OF EXECUTION', current_datetime()))
            writer.writerow(('NAME', 'URL', 'STATUS CODE', 'SATISFIED?', 'STRING', 'ELAPSED TIME'))
            writer_last.writerow(('NAME', 'URL', 'STATUS CODE', 'SATISFIED?', 'STRING', 'ELAPSED TIME'))

            for row in reader:
                if rownum != 0:  # escape header
                    logging.info('{} => '.format(row[0]) + str(monitor_site(row[1], row[2])))
                    live, satisfy, elapsed_time = monitor_site(row[1], row[2])
                    writer.writerow((row[0], row[1], live, satisfy, row[2], elapsed_time))
                    writer_last.writerow((row[0], row[1], live, satisfy, row[2], elapsed_time))
                    print('checking ' + row[0] + '...')

                rownum += 1
            writer.writerow(('\n' + '='*50 + '\n',))
            handle_write.close()
            handle_write_last.close()
            logging.info('write completed. log file is ready')
            print('')
        time.sleep(interval)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nThank you\nWhy don\'t you check your logs now')
        sys.exit(0)
    except FileNotFoundError:
        print('File Not Found. Please enter an existing file name with the csv extension')
        sys.exit(1)
