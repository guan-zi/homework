# -*- coding=utf-8 -*-

import urllib2
# 代理地址从西刺获得
autoproxy_handler = urllib2.ProxyHandler({"http": "114.229.69.78:808"})

opener = urllib2.build_opener(autoproxy_handler)

request = urllib2.Request("http://www.baidu.com")

response = opener.open(request)
print response.read()
