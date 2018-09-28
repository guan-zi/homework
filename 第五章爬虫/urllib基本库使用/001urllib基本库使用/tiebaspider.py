# !/usr/bin/env python
# -*- coding=utf-8 -*-
import urllib
import urllib2

def loadPage(fullurl, filename):
	print "正在下载 " + filename
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/65.0.3325.181 Chrome/65.0.3325.181 Safari/537.36'}
	
	request = urllib2.Request(fullurl, headers=headers)
	response = urllib2.urlopen(request)
	return response.read()

def writePage(html, filename):
	print "正在保存 " + filename
	with open(filename, 'w')as f:
		f.write(html)
	print '*'*20

def tiebaSpider(fullurl, beginPage, endPage):
	"""
        作用：贴吧爬虫调度器，负责组合处理每个页面的url
        url : 贴吧url的前部分
        beginPage : 起始页
        endPage : 结束页
    """
	for page in range(beginPage, endPage + 1):
		pn = (page - 1)*50
		filename = "第" + str(page) + "页.html"
		fullurl = url + '&pn' + str(pn)
		
		html = loadPage(fullurl, filename)
		
		writePage(html, filename)
	
	print "谢谢使用"


if __name__ == '__main__':
	kw = raw_input('请输入需要爬取的贴吧名:')
	beginPage = int(raw_input('请输入起始页：'))
	endPage = int(raw_input('请输入结束页：'))

	url = 'https://tieba.baidu.com/f?'
	key = urllib.urlencode({'wd': kw})
	fullurl = url + key
	tiebaSpider(fullurl, beginPage, endPage)