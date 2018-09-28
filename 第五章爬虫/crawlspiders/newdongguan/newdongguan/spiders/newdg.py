# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spider import CrawlSpider, Rule
from newdongguan.items import NewdongguanItem


class NewdgSpider(CrawlSpider):
    name = 'newdg'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=']
    pagelink = LinkExtractor(allow=r'type=4')
    contentlink = LinkExtractor(allow=r'/html/question/\d+/\d+.shtml')
    
    rules = (
        Rule(pagelink, process_links="deal_link"),
        Rule(contentlink, callback="parse_item"))
    # links 是当前response里面提取出来的链接列表
    def deal_link(self, links):
        for each in links:
            each.url = each.url.replace('?', "&").replace('Type&', 'Type?')
        return links

    def parse_item(self, response):
        item = NewdongguanItem()
        # 标题
        item['title'] = response.xpath('//div[contains(@class,"pagecenter p3")]//strong/text()').extract()[0]
        # 编号
        item['number'] = item['title'].split(' ')[-1].split(':')[-1]
        # 内容，先使用图片情况下的匹配规则，如果有内容，返回搜有内容列表
        content = response.xpath('//div[@class="contenttext"]/text()').extract()
        # 如果没有内容，则返回空列表，则使用无图片情况下的匹配规则
        if len(content) == 0:
            content = response.xpath('//div[@class="c1 text14_2"]/text()').extract()
            item['content'] = ''.join(content).strip()
        else:
            item['content'] = ''.join(content).strip()
        # 链接
        item['url'] = response.url
        yield item
