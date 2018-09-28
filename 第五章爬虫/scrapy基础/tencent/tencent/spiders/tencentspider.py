# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem

class TencentspiderSpider(scrapy.Spider):
    name = 'tencentspider'
    allowed_domains = ['tencent.com']
    url = 'http://hr.tencent.com/position.php?keywords=&tid=0&start='
    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):
        for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
            item = TencentItem()
            item['jobName'] = each.xpath('./td[1]/a/text()').extract()[0]
            item['jobLink'] = each.xpath('./td[1]/a/@href').extract()[0]
            item['jobType'] = '' if len(each.xpath('./td[2]/text()').extract()) == 0 else each.xpath('./td[2]/text()').extract()[0]
            #item['jobType'] = each.xpath('./td[2]/text()').extract()[0]
            item['jobNum'] = each.xpath('./td[3]/text()').extract()[0]
            item['jobLocation'] = each.xpath('./td[4]/text()').extract()[0]
            item['publishTime'] = each.xpath('./td[5]/text()').extract()[0]
            
            yield item
        if self.offset < 3610:
            self.offset += 10
        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
