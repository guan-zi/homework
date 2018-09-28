# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from doubanmovies.items import DoubanmoviesItem


class DoubanClassicMoviesSpider(CrawlSpider):
    name = 'douban_classic_movies'
    allowed_domains = ['movie.douban.com']
    offset = 0
    urls = 'https://movie.douban.com/explore#!type=movie&tag=%E7%BB%8F%E5%85%B8&sort=rank&page_limit=20&page_start='
    start_urls = [urls+str(offset)]

    # page_link = LinkExtractor(allow=r'page_limit=\d+&page_start=\d+')
    movie_link = LinkExtractor(allow=r'subject/\d+')

    rules = (
        Rule(movie_link, callback='parse_movie'),
    )

    def parse_movie(self, response):
        # i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i
        item = DoubanmoviesItem()
        #for movie_link in
        item['name'] = response.xpath('//h1/span/text()').extract()[0]
        item['director'] = response.xpath('//div/span/span/a[@rel]/text()').extract()[0]
        item['cast'] = response.xpath('//span/span/a[@rel="v:starring"]/text()').extract()[:]
        item['stars'] = response.xpath('//strong/text()').extract()[0]
        item['qoute'] = response.xpath('//span[@class="short"]/span/text()').extract()[0]

#        yield item
#        self.offset += 20
#        yield scrapy.Request(urls+str(self.offset)) 

