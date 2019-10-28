# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class SpSpider(CrawlSpider):
    name = 'sp'
    allowed_domains = ['gushiwen.org']
    start_urls = ['https://www.gushiwen.org/']

    rules = (
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'https://so.gushiwen.org/gushi/.*?.aspx', restrict_xpaths=('//div[@class="cont"]')),
             callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        i['name'] = response.xpath('//div[@class="typecont"]//span/a/text()').extract()[0]
        # print(i)
        # i['title'] = response.xpath('//input[@id="sid"]/@value').extract()
        # i['content'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
