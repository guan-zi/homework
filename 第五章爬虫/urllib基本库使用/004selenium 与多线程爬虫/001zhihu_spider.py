# -*- coding=utf-8 -*-

import urllib.request
import bs4
import re
import urllib.parse


url = "https://accounts.douban.com/login"

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
}
#获得登录页面信息
# request = urllib.request.Request(url)

html = urllib.request.urlopen(url).read().decode("utf-8")
# print(html)
soup = bs4.BeautifulSoup(html, "lxml")
# 获得验证码链接及验证码id
tag = soup.find_all(id="captcha_image")
for content in tag:
    captcha_link = str(content["src"])
    pattarn = re.compile("id=(.*?)&")
    id = pattarn.search(captcha_link).group(1)

captcha_data = urllib.request.urlopen(captcha_link).read()
# 保存验证码图片
with open("captcha.jpg", "wb") as f:
    f.write(captcha_data)
#人工识别后输入验证码
captcha = input("请输入验证码：")

data = {
    "source": None,
    "redir": "https://movie.douban.com/",
    "form_email": "930045665@qq.com",
    "form_password": "ghming1520",
    "captcha-solution": captcha,
    "captcha-id": id,
    "login": "登录"
}
data = urllib.parse.urlencode(data)

print(data)
headers2 = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Length': '193',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'll="118267"; bid=F_Q2qTYXNS8; _vwo_uuid_v2=D2CCB8F8E012498203494AB707E3A2FBF|3c9880a8af713c3c34cc5f055885a837; __utma=30149280.1614485568.1531269826.1531451082.1532008630.3; __utmc=30149280; __utmz=30149280.1532008630.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ap=1; ps=y; ue="930045665@qq.com"; dbcl2="181443807:P9Tna1M46Ik"; ck=c6dB; push_noty_num=0; push_doumail_num=0',
    'Host': 'accounts.douban.com',
    'Origin': 'https://accounts.douban.com',
    'Referer': 'https://accounts.douban.com/login',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/67.0.3396.99 Chrome/67.0.3396.99 Safari/537.36',
}
print(urllib.request.urlopen(url, data=data).read())