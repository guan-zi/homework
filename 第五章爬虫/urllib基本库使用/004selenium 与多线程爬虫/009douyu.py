import unittest
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.chrome.options import Options
import time

class douyu(unittest.TestCase):
    # 初始化方法，必须是setUp()
    def setUp(self):
        option = Options()
        option.add_argument('--headless')
        self.driver = webdriver.Chrome(chrome_options=option)
        self.num = 0
        self.count = 0
        self.page = 1

    # 测试方法必须有test字样开头
    def testDouyu(self):
        self.driver.get("https://www.douyu.com/directory/all")

        while True:
            soup = bs(self.driver.page_source, 'lxml')

            names = soup.find_all('h3',attrs={'class': 'ellipsis'})

            numbers = soup.find_all('span',attrs={'class': 'dy-num'})

            for name, number in zip(names, numbers):
                print('当前直播间%s'%name.get_text().strip())
                print('观众人数%s'%number.get_text().strip())
                self.num += 1
                count = number.get_text().strip()
                print('')
                if count[-1] == '万':
                    count = float(count[:-1])*10000
                    self.count += count
                    continue
                self.count += int(number.get_text().strip())
            print(self.page)
            if self.driver.page_source.find('shark-pager-disable-next') != -1:
                # 查看find源码发现如果在当前页找不到返回-1,如果找到及翻到最后一页，退出循环
                break
            self.driver.find_element_by_class_name('shark-pager-next').click()

            self.page += 1
            time.sleep(2)

    # 测试结束执行的方法
    def tearDown(self):
        print('当前直播网站直播人数%d'%self.num)
        print('当前网站观众人数%0.1f万人'%(self.count/10000))
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

