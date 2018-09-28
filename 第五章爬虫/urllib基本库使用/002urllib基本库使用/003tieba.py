# -*- coding=utf-8 -*-
import urllib
import urllib2

def loadPage(url, filename):
    """
    :param url: 根据url发送请求，获取服务器响应文件
    :param filename: 处理的文件名
    :return:
    """
    print "正在下载" + filename
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}
    request = urllib2.Request(url, headers=headers)

    return urllib2.urlopen(request).read()

def writePage(html, filename):
    """
    :param html:将html内容写入到本地
    :param filename: 服务器响应文件内容
    :return:
    """
    print "正在保存" + filename
    with open(filename, "w") as f:
        f.write(html)
    print "-"*10


def tiebaSpider(url, beginPage, endPage):
    """

    :param url: 贴吧网址前部分
    :param beginPage: 起始页
    :param endPage: 结束页
    :return:
    """
    for page in range(beginPage, endPage+1):
        pn = (page-1)*50
        filename = "第" + str(page) + "页.html"
        html = loadPage(fullurl, filename)
        writePage(html, filename)
        print "谢谢使用！"


if __name__ == '__main__':
    kw = raw_input("请输入需要爬去的贴吧名：")
    beginPage = int(raw_input("请输入起始页："))
    endPage = int(raw_input("请输入结束页："))

    url = "http://tieba.baidu.com/f?"
    key = urllib.urlencode({'kw': kw})
    fullurl = url + key
    tiebaSpider(fullurl, beginPage, endPage)