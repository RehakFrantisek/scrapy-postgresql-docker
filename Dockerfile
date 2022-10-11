FROM python:3
WORKDIR /usr/src/app
COPY . .
RUN pip install scrapy
CMD (cd /usr/src/app/srealityscraper && scrapy crawl srealityspider -O sreality.json)
