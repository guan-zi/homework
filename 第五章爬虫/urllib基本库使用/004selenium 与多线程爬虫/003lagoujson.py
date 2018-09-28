# -*- coding=utf-8 -*-

import urllib.request
import json
import jsonpath

url = "http://www.lagou.com/lbs/getAllCitySearchLabels.json"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

request = urllib.request.Request(url, headers=headers)

response = urllib.request.urlopen(request)
#  取出json文件里的内容，返回的格式是bytes
html = response.read()
# 把json形式的bytes转换为utf-8字符串
unicode_str = json.loads(html.decode("utf-8"))
# Python形式的列表
city_list = jsonpath.jsonpath(unicode_str, "$..name")
# dumps()默认中文为ascii编码格式，ensure_ascii默认为True
# 禁用ascii编码格式，返回的Unicode字符串，方便使用
array = json.dumps(city_list, ensure_ascii=False)

with open("lagoucity.json", "w") as f:
    f.write(array)