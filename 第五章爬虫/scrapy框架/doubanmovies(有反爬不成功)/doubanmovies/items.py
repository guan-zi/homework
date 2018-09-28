# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanmoviesItem(scrapy.Item):
    # define the fields for your item here like:
    # 片名
    name = scrapy.Field()
    # 评分
    stars = scrapy.Field()
    # 导演
    director = scrapy.Field()
    # 演员表
    cast = scrapy.Field()
    # 简介
    quote = scrapy.Field()
    #pass
