# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    jobName = scrapy.Field()
    jobLink = scrapy.Field()
    jobType = scrapy.Field()
    jobNum = scrapy.Field()
    jobLocation = scrapy.Field()
    publishTime = scrapy.Field()
    
