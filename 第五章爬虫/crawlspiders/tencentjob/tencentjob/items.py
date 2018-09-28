# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentjobItem(scrapy.Item):
    # define the fields for your item here like:
    # 职位名
    positionname = scrapy.Field()
    # 详情链接
    positionlink = scrapy.Field()
    # 职位类别
    positiontype = scrapy.Field()
    # 招聘人数
    positionnum = scrapy.Field()
    # 工作地点
    worklocation = scrapy.Field()
    # 发布时间
    publishtime = scrapy.Field()
    # pass
