# monitor-website
Monitors given websites for being live/down and if satisfies requirements


## Website Part
In order to run the server => `gunicorn application:app`


Now website is being served on localhost:8000

## Command Line Part
You can start the program with => `./monitor.py`
program takes 2 optional command line arguments
        * arg1 -- time interval in seconds. Default: 10 seconds. For example `./monitor.py 60`
        * arg2 -- configuration file in csv extension. Default: config.csv for example `./monitor.py 15 my_config_file.csv`
            Please note to create a header line if custom config file is given.(Or just fill the first line with dummy data)
