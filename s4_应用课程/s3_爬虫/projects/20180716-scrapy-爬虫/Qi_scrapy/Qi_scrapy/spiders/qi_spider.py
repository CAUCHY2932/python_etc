# -*- coding: utf-8 -*-
import scrapy


class QiSpiderSpider(scrapy.Spider):
    name = 'qi_spider'
#    allowed_domains = ['www.qichacha.com']
    start_urls = ['http://www.qichacha.com/']

    def parse(self, response):
       # pass
       # fileName=response.url
