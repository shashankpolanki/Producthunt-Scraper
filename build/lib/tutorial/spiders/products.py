import scrapy

class productsSpider(scrapy.Spider):
    name = "product"
    start_urls = ['http://producthunt.com/']

    def parse(self, response):
        theTool = response.css('div.item_54fdd').extract_first()
        yield{
            'name': theTool.css('h2::text').extract_first(),
            'description': theTool.css('h3::text').extract_first()
        }
