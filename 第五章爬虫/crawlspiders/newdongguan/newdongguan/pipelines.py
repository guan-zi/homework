# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs


class NewdongguanPipeline(object):
    def __init__(self):
        self.filename = codecs.open('newdg.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        # content = json.dumps(dict(item), ensure_ascii=False) + '\n'
        content = json.dumps(dict(item)) + '\n'
        # self.filename.write(content)        
        self.filename.write(content.encode('ascii').decode('unicode_escape'))        
        return item

    def close_spider(self, spider):
        self.filename.close()
