# -*- coding=utf-8 -*-

import urllib
import urllib2

url = "http://www.baidu.com/s?"
headers = {"User-Agent": "Mozilla"}

keyword = raw_input("请输入需要查询的关键字：")

kw = {"wd": keyword}

kw = urllib.urlencode(kw)
print kw
fullurl = url + kw

request = urllib2.Request(fullurl, headers=headers)

response = urllib2.urlopen(request)

print response.read()