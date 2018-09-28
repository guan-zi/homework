# -*- coding=utf-8 -*-

import urllib2
import ssl

https_handler = urllib2.HTTPSHandler(debuglevel=1)

opener = urllib2.build_opener(https_handler)

url = "http://www.12306.cn/mormhweb/"
# context = ssl._create_unverified_context()

request = urllib2.Request(url)
# 与urlopen()区别，不需要context证书
response = opener.open(request)

print response.read()
