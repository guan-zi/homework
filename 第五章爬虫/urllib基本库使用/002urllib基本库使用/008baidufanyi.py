# -*- coding=utf-8 -*-

import urllib2
import urllib
import json


url = "http://fanyi.baidu.com/sug"

headers = {
    # "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Host": "fanyi.baidu.com",
    "Origin": "http://fanyi.baidu.com",
    "Referer": "http://fanyi.baidu.com/?aldtype=16047",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/66.0.3359.181 Chrome/66.0.3359.181 Safari/537.36",
    # "X-Requested-With": "XMLHttpRequest"
}

keyword = raw_input("请输入要查询的词汇：")

form_data = {"kw": keyword}
form_data = urllib.urlencode(form_data)
print form_data

request = urllib2.Request(url, data=form_data, headers=headers)

# print urllib2.urlopen(request).read()
response = urllib2.urlopen(request)
# 获得数据编码格式为Unicode,此处使用unicode_escape解码
print response.read().decode("unicode_escape")
# html = response.read()
# print html


# json_data = json.load(response.read().decode("unicode_escape"))
# print json_data

