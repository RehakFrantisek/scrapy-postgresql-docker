FROM python:3
WORKDIR /usr/src/app
COPY . .
# TODO odstranit
#CMD (cd /usr/src/app/srealityscraper && scrapy crawl srealityspider -O sreality.json)