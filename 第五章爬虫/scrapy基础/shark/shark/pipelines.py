# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline
import os


class SharkPipeline(ImagesPipeline):

    # 创建一个ImagesPipeline的子类用于处理，图片文件
    # def process_item(self, item, spider):
    #    return item
    # 从settings文件中获得文件存储路径
    IMAGES_STORE = get_project_settings().get('IMAGES_STORE')
    
    def get_media_requests(self, item, info):
        image_url = item['imagelink']
        yield scrapy.Request(image_url)

    def item_completed(self, result, item, info):
        image_path = [x['path'] for ok, x in result if ok]
        
        os.rename(self.IMAGES_STORE + '/' + image_path[0], self.IMAGES_STORE + '/' + item['nickname'] + '.jpg')
        item['imagepath'] = self.IMAGES_STORE + '/' + item['nickname']
        return item
