#-*- coding=utf-8 -*-
#!/usr/bin/env python

import urllib
import urllib2
import ssl

# 忽略SSL安全认证
context = ssl._create_unverified_context()

url = 'http://www.12306.cn/mormhweb/'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/65.0.3325.181 Chrome/65.0.3325.181 Safari/537.36'}

request = urllib2.Request(url, headers=headers)

print urllib2.urlopen(request,context=context).read()
