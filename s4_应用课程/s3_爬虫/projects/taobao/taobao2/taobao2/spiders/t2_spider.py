# -*- coding: utf-8 -*-
import scrapy


class T2SpiderSpider(scrapy.Spider):
    name = 't2_spider'
    allowed_domains = ['www.taobao.com']
    start_urls = ['http://www.taobao.com/']

    def parse(self, response):
        pass
