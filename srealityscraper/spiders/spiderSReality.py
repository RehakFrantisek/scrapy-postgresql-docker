import scrapy

class WebSpider(scrapy.Spider):
    name = 'srealityspider'
    start_urls = ['https://www.sreality.cz/hledani/byty/prodej?_escaped_fragment_=']
    custom_settings = {
        'USER_AGENT':'Frantisek Rehak',
        'AUTOTHROTTLE_ENABLED': True,
        'AUTOTHROTTLE_START_DELAY': 0.5,
        #'CLOSESPIDER_ITEMCOUNT': 500,
        #'DOWNLOAD_DELAY': 0.1,
        #'RANDOMIZE_DOWNLOAD_DELAY' : False,
    }

    def parse(self, response):
        for properties in response.css("div[class='property ng-scope']"):
            try:

                yield{
                    'title': properties.css("a.title span[class='name ng-binding']::text").get(),
                    'image_url': properties.css("a._2vc3VMce92XEJFrv8_jaeN img::attr(src)").get(),
                }
            except:
                print("parse error")

    '''def parse(self, response):

        for image_url in response.css(''):
            try:
            
            
            image
            response.css("a._2vc3VMce92XEJFrv8_jaeN img::attr(src)").extract()
            
            nahradni -- response.css('.ng-scope img::attr(src)').extract()  
            
            
            title 
            response.css("a.title span[class='name ng-binding']::text").extract()

            properties
            response.css("div[class='property ng-scope']::text")

'''