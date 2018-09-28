# -*- coding=utf-8 -*-
# !/usr/bin/env python3


import urllib.request
import urllib.parse

url = "http://www.baidu.com/s"
word = {"wd": "传智播客"}
word = urllib.parse.urlencode(word)
new_url = url + "?" + word

headers = {
    "User-Agent": "Mozilla/5.0\
    (Windows NT 10.0; WOW64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
request = urllib.request.Request(new_url, headers=headers)

response = urllib.request.urlopen(request)
# response.获得的数据为bytes类型，使用decode()解码
# print(response.read().decode())
# 将获得的数据写入指定文件内
with open("chuanzhi2.html", "a") as f:
    f.write(response.read().decode())
