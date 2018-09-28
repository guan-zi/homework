# -*- coding=utf-8 -*-


from bs4 import BeautifulSoup
import requests
import time

def captcha(captcha_data):
    with open("captcha.jpg", "wb") as f:
        f.write(captcha_data)

    text = input("请输入验证码：")

def zhihuLogin():
    sess = requests.Session()

    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

    html = sess.get("https://www.zhihu.com/#signin", headers=headers).text

    bs = BeautifulSoup(html, 'lxml')

    _xsrf = bs.find("input", attrs={"name": "_xsrf"}).get("value")
    captcha_url = "https://www.zhihu.com/captcha.gif?r=%d&type=login" % (time.time() * 1000)

    captacha_data = sess.get(captcha_url, headers=headers).content

    text = captcha(captacha_data)

    data = {
        "_xsrf" : _xsrf,
        "email" : "123636274@qq.com",
        "password" : "ALARMCHIME",
        "captcha" : text
    }

    response = sess.post("https://www.zhihu.com/login/email", data = data, headers = headers)

    response = sess.get("https://www.zhihu.com/people/maozhaojun/activities", headers = headers)

    with open("my.html", "w") as f:
        f.write(response.text)

if __name__ == '__main__':
    zhihuLogin()