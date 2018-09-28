#!/usr/bin/env python
# -*- coding=utf-8 -*-

import urllib2

url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=ubuntuu_cb&wd=sublime%20%E8%B0%83%E8%AF%95&oq=%25E8%25B1%2586%25E7%2593%25A3%25E7%259F%25AD%25E8%25AF%2584&rsv_pq=90d2e4ee00051818&rsv_t=34eb%2BlNY6uq1LwKV%2BiVka1wIPCTulZdjbiHu8rX54ADyoiTDoa9jD3f0qctL7B%2BKEA&rqlang=cn&rsv_enter=1&rsv_sug3=20&rsv_sug1=18&rsv_sug7=101&rsv_sug2=0&inputT=11604&rsv_sug4=12690'
ua_headers = {
	'User-Agent': 'Mozilla/5.0 \
	(X11; Linux x86_64) AppleWebKit/537.36 \
	(KHTML, like Gecko) Ubuntu Chromium/65.0.3325.181 \
	Chrome/65.0.3325.181 Safari/537.36'}

request = urllib2.Request(url, headers=ua_headers)
response = urllib2.urlopen(request)

html = response.read()
print html
