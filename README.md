# monitor-website
* Monitors web sites and reports their availability and verifies corresponding page
content requirements from a configuration file.
* Running `monitors.py`, creates a log.csv file that shows the progress of the periodic checks.
* The checking period (by seconds) is configurable via a command-line option like => `monitors.py 60`
* Single-page HTTP server interface is availabe via gunicorn, Flask with Jinja2 and Bootstrap.
* The time it took for the web server to complete the whole request, is logged to log.csv.
* Optinal csv file to read in can be given like `monitors.py 60 my_config_file.csv`
If not given, default `config.csv` will be used for reading in.


## Website Part
I used Flask with Jinja2, and Bootstrap for a nice visualization.


Only the last most current periodic check is displayed on the website.


gunicorn is chosen to serve the website. If you don't have gunicorn, just do `pip3 install gunicorn` in terminal.


You can start the server by typing in your terminal while in the project's file system => `gunicorn application:app`


Now website is being served on localhost:8000

## Command Line Part
All periodic checks are stored on log.csv.


You can start the program by typing in your terminal while in the project's file system => `./monitor.py`


program takes 2 optional command line arguments:


* arg1 -- time interval in seconds. Default: 10 seconds. For example `./monitor.py 60`
* arg2 -- configuration file in csv extension to read in. Default: config.csv for example `./monitor.py 15 my_config_file.csv`

  Please note **if custom config file is given** (*if you use default config.csv, no need to do anything*), custom file's first line shouldn't contain any data. Because that's 
  reserved for header row.
  
  
  Filling up with header info like => name, url etc.. is advised.
  (Or just fill the first line with dummy data) 
  Program will start checking, starting from 2nd line.
  
  
  Last thing to note is that, **custom config file** shouldn't have any empty lines.


Thank you