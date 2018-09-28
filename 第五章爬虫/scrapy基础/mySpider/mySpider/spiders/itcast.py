# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import ItcastItem


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#']

    def parse(self, response):
        # 存放老师信息的集合
        #items = []
        for each in response.xpath('//div[@class="li_txt"]'):
            # 将得到的数据封装到‘ItcastItem’对象
            item = ItcastItem()
            # extract()方法返回的都是unicode字符串
            name = each.xpath('h3/text()')[0].extract()
            title = each.xpath('h4/text()')[0].extract()
            info = each.xpath('p/text()')[0].extract()
            # xpath返回的是包含一个元素的列表
            item['name'] = name
            item['title'] = title
            item['info'] = info
            
            #items.append(item)
            yield item
        # 返回最后的数据
        #return items
