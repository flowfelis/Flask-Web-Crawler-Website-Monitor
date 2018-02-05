# monitor-website
Monitors given websites for being live/down and if satisfies requirements


## Website Part
I used Flask on the back-end, and Bootstrap on the front-end for nice visualization.


Only the last most current periodic check is displayed on the website.


gunicorn is chosen to serve the website. Therefore you need to have gunicorn installed on your system.
If you don't, just do `pip3 install gunicorn`


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
  

Thank you