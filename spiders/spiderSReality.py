import scrapy

class BlogSpider(scrapy.Spider):
    name = 'srealityspider'
    start_urls = ['https://www.sreality.cz/hledani/prodej/byty']
    custom_settings = {
        'USER_AGENT':'Frantisek Rehak',
        'AUTOTHROTTLE_ENABLED': True,
        'AUTOTHROTTLE_START_DELAY': 0.5,
        #'CLOSESPIDER_ITEMCOUNT': 500,
        #'DOWNLOAD_DELAY': 0.1,
        #'RANDOMIZE_DOWNLOAD_DELAY' : False,
    }

    def getTitle(self, response):
        for tag in response.css('a title'):
            yield tag.css('::text').extract_first().strip().lower()

    def parse(self, response):

        for image_url in response.css(''):
            try:
