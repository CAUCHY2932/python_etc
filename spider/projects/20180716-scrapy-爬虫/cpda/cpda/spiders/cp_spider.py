# -*- coding: utf-8 -*-
import scrapy


class CpSpiderSpider(scrapy.Spider):
    name = 'cp_spider'
    allowed_domains = ['ai.datahoop.cn']
    start_urls = ['http://ai.datahoop.cn/']

    def parse(self, response):
        pass
