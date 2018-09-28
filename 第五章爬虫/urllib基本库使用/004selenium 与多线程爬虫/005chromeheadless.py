# -*- coding=utf-8 -*-

from selenium.webdriver.chrome.options import Options


# global DRIVER
# chrome_options = Options()
# chrome_options.add_argument("--disable-gpu")
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pymysql

def init_db():
    global CONNECTION
    CONNECTION = pymysql.connect("addr", "user_name", "passwd", "db", use_unicode=True, charset='utf-8')


def init_web_driver():
    global DRIVER

    # DRIVER = webdriver.PhantomJS(executable_path='C:\phantomjs-1.9.2-windows\phantomjs.exe')
    # DRIVER.set_window_size(1920, 1080)
    '''   
    dcap = dict(DesiredCapabilities.PHANTOMJS)

    dcap["phantomjs.page.settings.userAgent"] = (
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36"
    )

    dcap["phantomjs.page.settings.viewportSize"] = (
        "width: 1920, "
        "height: 1080"
    )

    DRIVER = webdriver.PhantomJS(executable_path='C:\phantomjs-1.9.2-windows\phantomjs.exe',desired_capabilities=dcap)
    DRIVER.set_window_size(1920, 1080)
    '''

    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument('--display-gpu')

    DRIVER = webdriver.Chrome(chrome_options=chrome_options)


def close_db():
    CONNECTION.close()


def close_web_driver():
    DRIVER.quit()


def login_taobao(username, password):
    DRIVER.get("https://member1.taobao.com/member/fresh/deliver_address.htm?spm=a1z08.2.0.0.7dad47611Wnj46")
    # DRIVER.get("https://login.taobao.com/member/login.jhtml?spm=a21bo.2017.201864-2.d1.7d2082a4FxukGr&f=top&redirectURL=http%3A%2F%2Fwww.taobao.com%2F")
    # 选择登陆方式
    DRIVER.find_element_by_xpath('//*[@id="J_Quick2Static"]').click()

    # login
    input_user = DRIVER.find_element_by_xpath('//*[@id="TPL_username_1"]')
    input_user.clear()
    input_user.send_keys(username)

    DRIVER.find_element_by_xpath('//*[@id="TPL_password_1"').send_keys(password)
    DRIVER.find_element_by_xpath('//*[@id=\"J_SubmitStatic\"]').click()

    time.sleep(0.5)


def get_data():
    # click to pick city
    # DRIVER.find_element_by_xpath('//*[@id="city-title"]').click()
    city_title = DRIVER.find_element_by_id("city-title")
    DRIVER.execute_script('arguments[0].click();', city_title)

    get_province_and_sub()


def get_province_and_sub():
    '''get province list'''
    province_items = DRIVER.find_element_by_name("city-province").find_elements_by_tag_name("a")

    for province_item in province_items:
        pid = province_item.get_attribute("attr-id")
        pname = province_item.get_attribute("title")
        if pid == "-1":
            print("continue province")
            continue

        sql = "insert into region_province_t (province_id, province) values('"+pid+"', '"+pname+"')"
        print(sql)
        cursor = CONNECTION.cursor()
        cursor.execute(sql)

        #province_item.click()
        DRIVER.execute_script('arguments[0].click();', province_item)
        time.sleep(0.5)

        get_city_and_sub(pid)
        back_tab(0)


def get_city_and_sub():
    '''get cities item'''
    city_items = DRIVER.find_element_by_class_name('city-city').find_elements_by_tag_name('a')
    for city_item in city_items:
        cid = city_item.get_attribute('attr-id')
        cname = city_item.get_attribute('title')
        if cid == '-1':
            print('continue city')
            continue

        sql = "insert into region_city_t (city_id, city, province_id) values('"+cid+"', '"+cname+"')"
        print(sql)
        cursor = CONNECTION.cursor()
        cursor.execute(sql)
        CONNECTION.commit()

        # city_item.click()
        DRIVER.execute_script('arguments[0].click();', city_item)
        time.sleep(1)

        get_area_and_sub()
        back_tab(1)


def get_area_and_sub(cid):
    '''get area and sub items'''
    area_items = DRIVER.find_element_by_class_name('city-district').find_elements_by_tag_name('a')
    for area_item in area_items:
        aid = area_item.get_attribute('attr-id')
        aname = area_item.get_attribute('title')

        if aid == '-1':
            print("continue area")
            continue

        sql = 'insert into region_area_ t (area_id,area,city_id) values('"+aid+"','"+aname"','"+cid+"')'
        print(sql)
        cursor = CONNECTION.cursor()
        cursor.execute(sql)
        CONNECTION.commit()

        #area_item.click()
        DRIVER.execute_script('arguments[0].click();',area_item)
        time.sleep(0.5)

        get_town_and_sub(aid)
        back_tab(2)


def get_town_and_sub(aid):
    '''get towns items'''
    town_items = DRIVER.find_element_by_class_name("city-street").find_elements_by_tag_name("a")
    for town_item in town_items:
        tid = town_item.get_attribute("attr-id")
        tname = town_item.get_attribute("title")
        if tid == "-1":
            print("continue town")
            continue

        sql = "insert into region_town_t (town_id,town,area_id) values('" + tid + "','" + tname + "','" + aid + "')"
        print(sql)
        cursor = CONNECTION.cursor()
        cursor.execute(sql)
        CONNECTION.commit()


def back_tab(index):
    districtEle = DRIVER.find_element_by_class_name("city-select-tab").find_elements_by_tag_name("a")[index]
    DRIVER.execute_script('arguments[0].click();', districtEle)
    time.sleep(0.5)

if __name__ == '__main__':
    init_db()
    init_web_driver()
    login_taobao('15274782328', 'ghm1520')
    get_data()
    close_db()
    close_web_driver()





