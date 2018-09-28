# -*- coding=utf-8 -*-

import urllib.request
from lxml import etree
import json
pg = 1
# pg = int(input("请输入要爬取得页码："))

url = "https://www.qiushibaike.com/8hr/page/%d/"%pg
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}


request = urllib.request.Request(url, headers=headers)
# 响应返回的是字符串，解析为HTML_DOM模式 text = etree.HTML(html)
html = urllib.request.urlopen(request).read()
text = etree.HTML(html)

# 返回所有段子的结点位置，contains()模糊查询方法，第一个参数是要匹配的标签，第二个参数是标签名部分内容
node_list = text.xpath("//div[contains(@id,'qiushi_tag')]")
# //div[@class="article block untagged mb15 typs_recent"]
# class="article block untagged mb15 typs_hot"]
# print(node_list)
items = {}
for node in node_list:
    # xpath返回的列表，这个列表就这一个参数，用索引方式取出来，用户名
    user_name = node.xpath(".//h2/text()")[0]
    # username = node.xpath('./div/a/@title')[0]
    # print(user_name)
    # 取出标签里包含的内容，点赞
    content = node.xpath("./a/div[@class='content']/span/text()")[0].strip()
    # content = node.xpath('.//div[@class="content"]/span')[0].text
    # print(content)
    # 图片连接
    image_link = node.xpath('./div[@class="thumb"]/a/img/@src')
    # print(image_link)
    zan = node.xpath('.//span[@class="stats-vote"]/i')[0].text
    # print(zan)
    # comments = node.xpath('.//span[@class="stats-vote"]/text()')
    # print(comments)
    comments = node.xpath('.//i/text()')
    # print(comments)
    items = {
        "user_name": user_name,
        "content": content,
        "image_link": image_link,
        "赞": zan,
        "评论": comments[1]
    }
    print(items)
    with open("qiushi.json", "a") as f:
        f.write(json.dumps(items, ensure_ascii=False)+'\n')