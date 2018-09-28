# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tencentjob.items import TencentjobItem


class TencentSpider(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    start_urls = ['http://hr.tencent.com/position.php?&start=0#a']
    pagerule = LinkExtractor(allow=r'start=\d+')
    
    rules = (
        Rule(pagerule, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):        
            item = TencentjobItem()
            item['positionname'] = each.xpath('./td[1]/a/text()').extract()[0]
            item['positionlink'] = each.xpath('./td[1]/a/@href').extract()[0]
            item['positiontype'] = each.xpath('./td[2]/text()').extract()[0]
            item['positionnum'] = '' if len(each.xpath('./td[3]/text()')) == 0 else each.xpath('./td[3]/text()').extract()[0]
            item['worklocation'] = each.xpath('./td[4]/text()').extract()[0]
            item['publishtime'] = each.xpath('./td[5]/text()').extract()[0]
            yield item
