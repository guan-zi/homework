# -*- coding=utf-8 -*-

import urllib
import urllib2
from lxml import etree


def loadPage(url):
    """
        作用:根据url发送请求，获取服务器响应文件
        url:需要爬取的地址
    """
    print "加载页面……"
    request = urllib2.Request(url)
    html = urllib2.urlopen(request).read()
    # 解析HTML文档为HTML DOM模型,即为xml文档
    content = etree.HTML(html)
    #print content
    #返回所有匹配成功的集合列表
    # 当使用xpath匹配目标为中文时，必须在匹配字符串最后面加/text()
    link_list = content.xpath('//div[@class="threadlist_title pull_left j_th_tit "]/a/@href')
    # print link_list
    for link in link_list:
        # print link.encode("utf-8")
        fulllink = "http://tieba.baidu.com" + link
        # print fulllink
        # 组合为每个帖子的链接
        loadImage(fulllink)


# 取出每个帖子里的每个图片链接
def loadImage(link):
    print "加载图片页面"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
    request = urllib2.Request(link, headers=headers)
    html = urllib2.urlopen(request).read()
    # 解析
    content = etree.HTML(html)
    # 取出帖子里每层曾主发送的图片连接集合
    #link_list = content.xpath()
    link_list = content.xpath('//img[@class="BDE_Image"]/@src')
    print link_list
    #link_list = content.xpath()
    for link in link_list:
        # print link.encode("utf-8")
        # fulllink = "http://tieba.baidu.com" + link
        print link
        writeImage(link)


def writeImage(link):
    """
        作用：将html内容写入到本地
        link:图片链接
    """
    print "保存图片"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

    request = urllib2.Request(link, headers=headers)
    image = urllib2.urlopen(request).read()

    filename = link[-10:]

    with open(filename, "wb") as f:
        f.write(image)
    print "已经成功下载" + filename



def tiebaSpider(url, beginPage, endPage):
    """
        作用：贴吧爬虫调度器，负责组合处理每个页面的url
        url: 贴吧url的前部分
        beginPage:起始页
        endPage:结束页
    """
    for page in range(beginPage, endPage):
        pn = (page - 1) * 50
        fullurl = url + "&pn=" + str(pn)

        loadPage(fullurl)

    print "感谢使用"


if __name__ == '__main__':
    kw = raw_input("请输入需要爬取的贴吧名：")
    beginPage = int(raw_input("请输入起始页："))
    endPage = int(raw_input("请输入结束页："))

    url = "http://tieba.baidu.com/f?ie=utf-8&"
    key = urllib.urlencode({"kw": kw})

    fullurl = url + key

    tiebaSpider(fullurl, beginPage, endPage)
