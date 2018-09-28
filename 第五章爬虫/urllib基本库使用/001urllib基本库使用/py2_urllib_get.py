#!/usr/bin/env python
# -*- coding=utf-8 -*-

import urllib
import urllib2

url = 'http://www.baidu.com/s'

headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/65.0.3325.181 Chrome/65.0.3325.181 Safari/537.36'}

keyword = raw_input('please input keyword:')
wd = {'wd': keyword}
wd = urllib.urlencode(wd)

fullurl = url + '?' + wd

request = urllib2.Request(fullurl, headers=headers)

response = urllib2.urlopen(request)

print response.read()
