# -*- coding=utf-8 -*-

import urllib
import urllib2
import random

ua_list = [
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
	'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/65.0.3325.181 Chrome/65.0.3325.181 Safari/537.36'
	]

user_agent = random.choice(ua_list)

url = 'http://www.baidu.com/'
# print user_agent

request = urllib2.Request(url)

#add_header()方法，添加/修改一个HTTP报头
request.add_header('User-Agent', user_agent)

print request.headers
#get_header()获取已有的HTTP报头的值，
#注意只能是第一个字母大写，其他小写

print request.get_header('User-Agent')
