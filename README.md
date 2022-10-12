# Luxonis python developer project

## Assignment
* Use scrapy framework to scrape the first 500 items (title, image url) from https://sreality.cz (flats, sell) and save it in the Postgresql database.
* Implement a simple HTTP server in python and show these 500 items on a simple page (title and image).
* Put everything to single docker-compose command so that I can just run "docker-compose up" in the Github repository and see the scraped ads on http://127.0.0.1:8080 page.


## Finished processes
* website -> scrapy
* scrapy -> json
* create table
* json -> insert script


## spider_sreality.py
* file to work with scrapy
* is it necessary to define some information (start_url, itemcount, ..)
* scrapes the defined data and scrolls to the next page


## loadjson.py
* stored json file is loaded as string
* string is appended to create-table.sql as insert script


## create-table.sql
* crete table in database
* insert into database


## docker-compose.yml
* services
  * app to run Dockerfile, define ports and also waiting for postgres service
  * postgres run the database, define host, user,password and values
* for testing I used adminer


## app.py
* used package psycopg2 to connect database
* created connection and executed data through flask


## templates folder
* base.html
  * defines CSS and its main template
* index.html
  * it is extension of base.html and there are defined records from database
