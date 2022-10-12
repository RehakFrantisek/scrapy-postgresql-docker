FROM python:3
WORKDIR /usr/src/app
COPY . .
RUN pip install -r requirements.txt
COPY . .
CMD set FLASK_APP=app
CMD flask run
# TODO odstranit
#CMD (cd /usr/src/app/srealityscraper && scrapy crawl srealityspider -O sreality.json)
#flask run -d 8080