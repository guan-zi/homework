# -*- coding=utf-8 -*-

import urllib
import urllib2
#从浏览器找到的请求地址需要验证，即复制到空地址栏，检查是否能得到结果.
url = "https://movie.douban.com/j/search_subjects?"

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
#找到请求地址后，在headers最下面Query String Parameters获得
query_data ={
    "type": "movie",
    "tag": "豆瓣高分",
    "page_limit": "50",
    "page_start": "0"
    }
query_data = urllib.urlencode(query_data)
print query_data

request = urllib2.Request(url, data=query_data, headers=headers)

response = urllib2.urlopen(request)
with open('douban.html', 'w') as f:
    f.write(response.read())

