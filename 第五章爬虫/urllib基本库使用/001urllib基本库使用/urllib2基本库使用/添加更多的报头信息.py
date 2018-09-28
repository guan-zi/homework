# -*- coding=utf-8 -*-


import urllib.request
# !/usr/bin/env python3

url = "http://www.itcast.cn"

header = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
request = urllib.request.Request(url, headers=header)

# 也可以通过调用Request.add_header() 添加/修改一个特定的header
request.add_header("Connection", "keep-alive")

# 也可以通过调用Request.get_header()来查看header信息
response = urllib.request.urlopen(request)
print(response.read())



