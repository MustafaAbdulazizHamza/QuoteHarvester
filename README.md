# QuoteHarvester
## Introduction
QuoteHarvester is a web scraper initially developed to extract the most popular quotes from the Goodreads website. The collected data can then be stored in a JSON file, XML, or MySQL database.

## Scrapy Framework
This project was created using the Scrapy Framework, a free and open-source web-crawling framework written in Python. Originally designed for web scraping, it can also be utilized for data extraction using APIs or as a general-purpose web crawler.

Scrapy Framework Website: https://scrapy.org/

## Requirements
1. All necessary Python packages are listed in the requirements.txt file. You can easily install them by using `pip install -r requirements.txt`
2. A MySQL server is required if you enable the feature of storing data in a database.

## First Step
To run the project, clone this repository and create a Python virtual environment to install the required packages. Consider modifying some important settings as per your requirements.

1. To store data in a database, you need to open the settings.py file and set the appropriate values for your MySQL server user credentials in the two variables: mySQLServerUsername and mySQLServerPassword. Also, enable data storage in the database by setting the enableDatabaseStorage flag to True.
2. To save data as a JSON file, remove the comments in the following text in the settings.py file:

 ```python
 FEEDS =  { 
            'output.json':{
               'format': 'json', 'overwrite': True            }
      }
```
## To Scrape
Run the following command after switching to your virtual environment and installing all requirements:
```bash
scrapy crawl QuoteSpider
```
