# -*- coding=utf-8 -*-
# !/usr/bin/env python3


import urllib.request
import urllib.parse


def tieba_spider(url, beignPage, endPage):
    """ 作用：负责处理url，分配每个url去发送请求
        url：需要处理的第一个url
        beginPage: 爬虫执行的起始页面
        endPage: 爬虫执行的截止页面
    """
    for page in range(beignPage, endPage):
        pn = (page-1)*50
        filename = "第" +str(pn) + "页.html"
        # 组合为完整的url，并且pn值每次增加50

        fullurl = url +"&pn=" + str(pn)
        # 调用loadPage()发送请求，获取HTML页面
        html = loadPage(fullurl, filename)

        wirteFile(html, filename)


def wirteFile(html, filename):
    """
    作用：保存服务器响应文件到本地磁盘文件里
    html: 服务器响应文件
    filename: 本地磁盘文件名
    """
    print("正在写入文件……")
    with open(filename, "w") as f:
        f.write(html)
    print("*"*20)


def loadPage(url, filename):
    """
    作用：根据url发送请求，获取服务器响应文件
    url：需要爬取的url地址
    filename: 文件名
    """
    print("正在下载……%s" % filename)
    header = {"User-Agent": "Mozilla/5.0\
     (compatible; MSIE 9.0;\
     Windows NT 6.1; Trident/5.0;"}

    request = urllib.request.Request(url, headers=header)
    response = urllib.request.urlopen(request)
    return response.read().decode()


if __name__ == '__main__':
    kw = input("请输入需要爬取的贴吧")
    beignPage = int(input("请输入起始页："))
    endPage = int(input("请输入终止页："))

    url = "https://tieba.baidu.com/f?"
    key = urllib.parse.urlencode({"kw": kw})

    url = url + key
    print(url)
    tieba_spider(url, beignPage, endPage)

