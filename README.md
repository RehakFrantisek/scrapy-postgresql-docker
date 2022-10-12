# Luxonis python developer project

## Assignment
* Use scrapy framework to scrape the first 500 items (title, image url) from https://sreality.cz (flats, sell) and save it in the Postgresql database.
* Implement a simple HTTP server in python and show these 500 items on a simple page (title and image).
* Put everything to single docker-compose command so that I can just run "docker-compose up" in the Github repository and see the scraped ads on http://127.0.0.1:8080 page.


## Postup prace
* scrapy -> data
* data -> json
* json -> insert script
* create + insert -> postgre


## spiderSReality.py
* tezba dat
* ulozeno do sreality.json

## loadjson.py
* nacteni jsonu preveden na string
* append do insert values (create-table.sql)

## create-table.sql
* crete table
* insert values

## docker-compose.yml
* services (app + postgre)
* pro testovani adminer

## HTTP.py
* sadasd

