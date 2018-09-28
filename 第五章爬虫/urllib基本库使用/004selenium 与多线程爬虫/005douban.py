# -*- coding=utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
# options.set_headless()
# options.add_argument("--disable-gpu")
# driver = webdriver.Chrome()
driver = webdriver.Chrome(executable_path="/media/guan/0F1112E40F1112E4/文档/黑马程序员/第五章爬虫/venv5/lib/python3.5/site-packages/selenium/webdriver/firefox/")
# driver = webdriver.PhantomJS(executable_path="/media/guan/0F1112E40F1112E4/文档/黑马程序员/第五章爬虫/venv5/lib/python3.5/site-packages/selenium/webdriver/phantomjs")
driver.get("https://movie.douban.com/typerank?type_name=剧情&type=11&interval_id=100:90&action=")

time.sleep(3)
# 向下滚动10000像素
js = "document.body.scrollTop=10000"
#js="var q=document.documentElement.scrollTop=10000"

driver.save_screenshot("douban.png")

driver.execute_script(js)

time.sleep(10)
driver.save_screenshot("newdouban.png")
driver.quit()
