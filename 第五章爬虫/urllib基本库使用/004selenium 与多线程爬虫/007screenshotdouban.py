from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
# 设置chromedriver Option
option = Options()
option.add_argument('--headless')

driver = webdriver.Chrome(chrome_options=option)

driver.get("https://movie.douban.com/typerank?type_name=剧情&type=11&interval_id=100:90&action=")

time.sleep(3)

js = 'document.body.scrollTop=10000'

driver.save_screenshot('douban.png')

driver.execute_script(js)
time.sleep(1)
driver.quit()
