# -*- coding=utf-8 -*-

from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
'''
    option = Options()
option.add_argument('--headless')

driver = webdriver.Chrome(chrome_options=option)
'''
option = Options()
option.add_argument('--headless')

driver = webdriver.Chrome(chrome_options=option)
driver.get('https://movie.douban.com/typerank?type_name=剧情&type=11&interval_id=100:90&action=')

time.sleep(3)
js = 'document.body'

driver.save_screenshot('douban.png')
driver.set_window_size(width=1600, height=800, windowHandle='current')
driver.execute_script(js)
time.sleep(10)
driver.save_screenshot("newdouban.png")

driver.quit()