# -*- coding=utf-8 -*-
# !/usr/bin/env python3


import urllib.request

import urllib.parse
import json
import time
import random
import hashlib

"""d：代表的是需要翻译的字符串。
f：当前时间的时间戳加上 0-10 的随机字符串。
u：一个常量——fanyideskweb。
c：一个常量——rY0D^0'nM0}g5Mm1z%1G4。
salt：就是f变量，时间戳。
sign：使用的是u + d + f + c的md5的值。
"""

content = input('请输入需要翻译的句子：')

url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=https://www.google.com/'

data = {}

u = 'fanyideskweb'
d = content
f = str(int(time.time()*1000) + random.randint(1, 10))
c = 'rY0D^0\'nM0}g5Mm1z%1G4'

sign = hashlib.md5((u + d + f + c).encode('utf-8')).hexdigest()

data['i'] = content
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['salt'] = f
data['sign'] = sign
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_CL1CKBUTTON'
data['typoResult'] = 'true'

headers = {
"Accept": "application/json, text/javascript, */*; q=0.01",
"Accept-Language": "zh-CN,zh;q=0.9",
"Connection": "keep-alive",
"Content-Length": "197",
"Host": "fanyi.youdao.com",
"Origin": "http://fanyi.youdao.com",
"Referer": "http://fanyi.youdao.com/",
"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/66.0.3359.181 Chrome/66.0.3359.181 Safari/537.36",
"X-Requested-With": "XMLHttpRequest"
}

data = urllib.parse.urlencode(data).encode('utf-8')
request = urllib.request.Request(url=url, data=data, headers=headers)
response = urllib.request.urlopen(request)

print(response.read().decode('utf-8'))

