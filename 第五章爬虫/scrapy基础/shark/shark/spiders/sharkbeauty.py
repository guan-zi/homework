# -*- coding: utf-8 -*-
import scrapy
import json
from shark.items import SharkItem 


class SharkbeautySpider(scrapy.Spider):
    name = 'sharkbeauty'
    allowed_domains = ['m.douyu.com']
    offset = 0
    url = 'https://m.douyu.com/api/search/getData?sk=%E7%BE%8E%E5%A5%B3&type=3&sort=1&limit=10&offset='
    start_urls = [url + str(offset)]

    def parse(self, response):
        #pass
        # 获得将response响应文件loads出，获得存储的列表数据
        data = json.loads(response.text)['data'].get('anchor')
        # 遍历出列表中存储的每个房间的字典文件
        for each in data:
            # 实例化对象文件
            item = SharkItem()
            # 获得数据
            item['nickname'] = each['roomName']
            item['imagelink'] = each['avatar']
            # item传给管道文件处理
            yield item

        #if self.offset < 80:
        # 偏移量自加，直至出allowed_domain
        self.offset += 10
        # 重新构造url, 使用回调函数再次执行
        yield scrapy.Request(self.url + str(self.offset), \
callback = self.parse)
