# -*- coding=utf-8 -*-
# !/usr/bin/env python3
import urllib.request

# 其中urllib2.urlopen()变成了urllib.request.urlopen()
# urllib2.Request()变成了urllib.request.Request()
request = urllib.request.Request("http://www.baidu.com/")
response = urllib.request.urlopen(request)

#response = urllib.urlopen(request)

print(response.read())


# 区别
# import urllib2

# request = urllib2.request(url)
# response = urllib2.urlopen(request)
# html = response.read()




