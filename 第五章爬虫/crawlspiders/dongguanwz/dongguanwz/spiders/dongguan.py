# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from dongguanwz.items import DongguanwzItem

class DongguanSpider(CrawlSpider):
    name = 'dongguan'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']

    rules = (
        Rule(LinkExtractor(allow=r'type=4&page=\d+')), 
        Rule(LinkExtractor(allow=r'/html/question/\d+/\d+.shtml'), callback='parse_item', follow=True)
    )

    def parse_item(self, response):
        #i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        #return i
        item = DongguanwzItem()
        item['title'] = response.xpath('//div[contains(@class, "pagecenter p3")]//strong/text()').extract()[0]
        item['number'] = item['title'].split(' ')[-1].split(':')[-1]
        item['content'] = response.xpath('//div[@class="c1 text14_2"]/text()').extract()[0]
        item['url'] = response.url
        yield item
