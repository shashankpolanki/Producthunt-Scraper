import scrapy

class productsSpider(scrapy.Spider):
    name = "product"
    start_urls = ['https://www.producthunt.com/']

    def parse(self, response):

        for i in range(5):

            theTool = response.css('div.item_54fdd')[i]
            yield {
                'name': theTool.css('h2::text').extract_first(),
                'description': theTool.css('h3::text').extract_first()
            }

    def parse_page2(self, response):
        item = response.meta['item']
        item['other_url'] = response.url
        return item




#linkElem = content.select('.item_54fdd a')[0]

#res2 = requests.get('https://www.producthunt.com' + str(linkElem.get('href')))

#res2.raise_for_status()

#content2 = bs4.BeautifulSoup(res2.text, "html.parser")

#linkElem2 = content2.select('.side_c0705 span')

#print('https://' + str(linkElem2[0].getText()))
