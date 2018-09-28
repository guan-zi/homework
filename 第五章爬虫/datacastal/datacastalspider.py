# -*- coding=utf-8 -*-

import urllib.request
from lxml import etree


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": "UM_distinctid=1640e2946b8e5-0b127f889b21f9-25004775-100200-1640e2946b9306; visitoruniquecookie=2aa757af-e322-416b-afe1-f01816468935_2018-07-16; TRAIN_SESSION=c600e054-66e5-4516-b172-3e412991a262; CNZZDATA1263227694=1678327180-1529245119-null%7C1531753226; SERVERID=ed7806043c88c9bcd32f6de7dfefdf48|1531755482|1531751829",
    "Host": "www.dcxueyuan.com",
    "Referer": "https://www.baidu.com/link?url=KVIDGk2i2zVi5vbss6WGd-OxlFWBJvum8E6oG4QVpgRhmqVcG8hFJ8kXxDIl3kWB&wd=&eqid=90de13000001b3ad000000065b4cbb5a",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/66.0.3359.181 Chrome/66.0.3359.181 Safari/537.36"
}

url = "https://www.dcxueyuan.com/mytrain/trainprocess/51589/17288/page.html"

request = urllib.request.Request(url, headers=headers)

html = urllib.request.urlopen(request).read()
print(html)
# content = etree.HTML(html)
