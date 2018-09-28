#!/usr/bin/env python
# -*- coding=utf-8 -*-

import urllib
import urllib2

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/65.0.3325.181 Chrome/65.0.3325.181 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
    }
#通过抓包工具获得的地址
#url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&smartresult=dict&smartresult=rule'
#以上是从浏览器获取的地址，地址不完整，运行有错误，
key = raw_input('请输入要翻译的词语：')
formdata = {
'i': key,
'from': 'AUTO',
'to': 'AUTO',
'smartresult': 'dict',
'doctype': 'json',
'keyfrom': 'fanyi.web',
'action': 'FY_BY_REALTIME',
'typoResult': 'true'
}

data = urllib.urlencode(formdata)

request = urllib2.Request(url, data=data, headers=headers)

print urllib2.urlopen(request).read()
#有报错









