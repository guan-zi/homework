# -*- coding=utf-8 -*-

import urllib
import urllib2
import re

class spider():
    def __init__(self):
        self.item_list = []

    def start_page(self):
        """设置起始爬取页面"""
        start_page = raw_input("please input the start page:")
        self.s_page = int(start_page)
        print "起始页为%s"%self.s_page

    def spider_active(self):
        """执行数据爬取任务"""
        url = "https://www.neihan8.com/article/list_5_"+str(self.s_page)+".html"
        headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}

        request = urllib2.Request(url, headers=headers)
        self.html = urllib2.urlopen(request).read().decode("gbk")
        print "页面已爬取"
        # print self.html

    def deal_content(self):
        """处理爬得数据"""
        # 编码转换前为ascii编码
        self.html = self.html.encode('utf8')
        # 正则表达式，增加re.S参数，补充.*不能够匹配的换行符
        pattarn = re.compile(r'<div\sclass="f18 mb20">(.*?)</div>', re.S)

        self.item_list = pattarn.findall(self.html)

        # print self.item_list



    def save_active(self):
        """将处理后数据写入文件"""
        print "正在写入……"

        for item in self.item_list:
            # print item
            item = item.replace("<p>", "").replace("</p>", "").replace("<br>", "").replace("<br />", "").replace(" ", "")

            with open("duanzi.txt", "a+") as f:
                f.write(item)
        print "页面已保存"

    def main(self):
        """主函数入口"""
        self.start_page()
        while True:
            self.spider_active()
            self.deal_content()
            self.save_active()
            command = raw_input("any key for continue,'quit' end the program:")
            if command == "quit":
                break
            self.s_page += 1
        print "byebye"

if __name__ == '__main__':
    duanzis_pider = spider()
    duanzis_pider.main()
