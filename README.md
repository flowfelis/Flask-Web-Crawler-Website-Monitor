# Monitor-Website 

## What Is It?

* This is a helper program for Website Administrators.
* It checks periodically websites that you defined in a .csv file.
* Logs them to log.csv file.
* Shows the last search results in a web page with a nice layout.

## How Is It Helpful?

* You can verify which websites are down or live.
* You can verify if a website has the string you were searching for, in the response.
* It creates a log file(log.csv) of all the websites it checked so far.
* It opens a website for you to check the last search results.
* Periodic checking time can be redefined in seconds.

## How To Use It?

* You need to have Python installed before using. You can install it [here](https://www.python.org/downloads/).
* Clone the repository to your file system.
* Run `./monitor.py` within terminal. You should be in the directory where you cloned.
    * Program will start with default parameters: 60 seconds interval time and input file of `config.csv`.
    * This will serve a website at _http://127.0.0.1:5000/_ (I used `Flask` and `Bootstrap`).
    * At the same time starts to fill up output log.csv file.
    * I used Python's `threading` module to run 2 tasks in one file.
* You can alternatively give 2 arguments:
    * first argument: interval time of periodic checks(seconds).
        * ie. -> `./monitor.py 120` (program runs, every 2 minutes.)
    * second argument: optional input .csv file.
        * ie. -> `./monitor.py 60 my_websites.csv` (program runs, every minute and reads from _my_websites.csv_)
* Hit `ctrl-c` to stop the program.

## Other Notes

  Please note **if custom config file is given** (*if you use default config.csv, no need to do anything*), custom file's first line shouldn't contain any data. Because that's 
  reserved for header row.
  
  
  Filling up with header info like => name, url etc.. is advised.
  (Or just fill the first line with dummy data) 
  Program will start checking, starting from 2nd line.
  
  
  Last thing to note is that, **custom config file** shouldn't have any empty lines.
  
  Feel free to fork or pull-request.
  
  
  Thank you
