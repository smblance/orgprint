from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.http import Request

from orgprint.items import Supply, Vendor


class OrgprintSuppliesSpider(Spider):
    name = "supplies"
    allowed_domains = ["orgprint.com"]
    start_urls = [
        "http://www.orgprint.com/kartridgi/"
    ]

    def parse(self, response):
        urls = response.css('.full_list .brand a::attr(href)').extract()
        # urls = [urls[6]]
        for next_url in urls:
            yield Request(response.urljoin(next_url), callback = self.parse_supply_url_follow_next_page)


    def parse_supply_url_follow_next_page(self, response):
        for supply_url in response.css('.consumable_info > a::attr(href)').extract():
            yield Request(response.urljoin(supply_url), callback = self.parse_supply)

        next_url = response.css('.next_class a::attr(href)').extract()
        if next_url:
            yield Request(response.urljoin(next_url[0]), callback = self.parse_supply_url_follow_next_page)



    def parse_supply(self, response):
        item = Supply()
        item['url'] = response.url

        item['data'] = dict()
        for div in response.css('.description'):
            for name, value in zip(div.css('.name div::text').extract(), div.css('.value div::text, .value a::text').extract()):
                item['data'].update({name: value})

        yield item
            
