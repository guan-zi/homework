# -*- coding=utf-8 -*-
#!/usr/bin/env python

import urllib
import urllib2

url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E6%82%AC%E7%96%91&sort=recommend'
#url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%BB%8F%E5%85%B8&sort=time&page_limit=20&page_start=0'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/65.0.3325.181 Chrome/65.0.3325.181 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Accept-Language': 'zh-CN,zh;q=0.9'
}
startpage = int(raw_input('请输入开始页：'))
#endpage = int(raw_input('请输入结束页：'))


formdata = {

    'page_limit': 50,
    'page_start': startpage,
    }

data = urllib.urlencode(formdata)

request = urllib2.Request(url, data=data, headers=headers)
response = urllib2.urlopen(request).read()

with open('douban.html', 'w') as f:
    f.write(response)
