# -*- coding: utf-8 -*-
import scrapy


class RenrenspiderSpider(scrapy.Spider):
    name = 'renrenspider'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    def parse(self, response):
        pass
