import scrapy

class WebSpider(scrapy.Spider):
    name = 'srealityspider'
    start_urls = ['https://www.sreality.cz/hledani/byty/prodej?_escaped_fragment_=&strana=1']
    custom_settings = {
        'USER_AGENT': 'Frantisek Rehak',
        'AUTOTHROTTLE_ENABLED': True,
        'AUTOTHROTTLE_START_DELAY': 0.5,
        'CLOSESPIDER_ITEMCOUNT': 500,
        'CLOSESPIDER_PAGECOUNT': 25
    }
    page_number = 1

    def parse(self, response):
        for properties in response.css("div[class='property ng-scope']"):
            try:
                yield {
                    'title': properties.css("a.title span[class='name ng-binding']::text").get(),
                    'image_url': properties.css("a._2vc3VMce92XEJFrv8_jaeN img::attr(src)").get(),
                }
            except:
                print("parse error")

        # TODO komentar
        self.page_number += 1
        next_page = f'https://www.sreality.cz/hledani/byty/prodej?_escaped_fragment_=&strana={self.page_number}'

        yield response.follow(next_page, callback=self.parse)