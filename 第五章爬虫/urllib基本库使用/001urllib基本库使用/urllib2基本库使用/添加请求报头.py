# -*- coding=utf-8 -*-

import urllib.request
# !/usr/bin/env python3

url = "http://www.itcast.cn"

ua_header = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}

request = urllib.request.Request(url, headers=ua_header)

response = urllib.request.urlopen(request)
print(response.code)
print(response.read())

