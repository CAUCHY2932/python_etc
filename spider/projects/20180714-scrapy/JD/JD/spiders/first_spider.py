# -*- coding: utf-8 -*-
import scrapy


class FirstSpiderSpider(scrapy.Spider):
    name = 'first_spider'
    allowed_domains = ['www.jd.com/']
    start_urls = ['http://www.jd.com//']

    def parse(self, response):
        pass
