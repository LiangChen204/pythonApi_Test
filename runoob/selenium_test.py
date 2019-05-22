#!//usr/local/bin python
# -*- coding:utf-8 -*-

"""
Created on 2019/5/8 15:33
@author: liangchen
@File: test
"""
import re
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# 淘宝登陆页面
# url = 'https://www.taobao.com/'
# 淘宝买家
# url = 'https://buyertrade.taobao.com/trade/itemlist/list_bought_items.htm?spm=a1z02.1.a2109.d1000368.74b9782dvDtV2a&nekot=1470211439694'
# 淘宝卖家
# url = 'https://myseller.taobao.com/home.htm'
# 运营后台
url = 'https://api.l.whereask.com/park_daily/presell-admin/page/index.html#/login/index'
chrome_options = Options()
# chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get(url)
print('打开浏览器')
# print(driver.title)
# driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/form/div[1]/input').send_keys('admin')
# driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/form/div[2]/input').send_keys('admin123')
# driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/form/button').click()
print('登录成功')
time.sleep(1)
# 构造cookie_dict
# 运营后台
cookie_dict = {
    'domain': 'api.l.whereask.com',
    'httpOnly': True,
    'name': 'token',
    'path': '/',
    'secure': False,
    'value': '79c22f62-0564-4920-a148-9147fc41e91a'
}
driver.add_cookie(cookie_dict)
# driver.refresh()
driver.get('https://api.l.whereask.com/park_daily/presell-admin/page/index.html#/advance/active/shop')
time.sleep(1)
down_icon = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div/div/div[1]/div[2]/div[1]/div/span')
print(type(down_icon))
down_icon.click()
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div/div/div[1]/div[2]/div[2]/ul[2]/li[2]').click()
print('下拉框点击成功')
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div/div/div[1]/button[1]').click()
print('查询成功>>>>>>>>>>>>>>>>>')
time.sleep(2)
# 获取该网页的源码
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
# # 获取两条以/wiki/开头的a标签的href属性
# listUrls = soup.findAll("a", href=re.compile("^/wiki/"), limit=2)
spans = soup.find_all(name='img')
# shop_list = []
for shop in spans:
    # print(shop)
    if shop.find_previous_sibling():
        # print(shop)
        # find_previous_sibling()返回前面第一个兄弟节点
        a = shop.find_previous_sibling().string
        # shop_list = shop_list.append(str(a))
        print(a)
# i = 0
# if i < len(shop_list):
#     elmenet = '/html/body/div[1]/div/div[2]/div/div[3]/div/div/div[2]/div/div[2]/div[1]/div/div/div[2]/table/tbody/tr[' + i + ']/td[1]/div/label/span/input'
#     i += 1
#     driver.find_element_by_xpath(elmenet).click()
#     time.sleep(1)

# b = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div/div/div[2]/div/div[2]/div[1]/div/div/div[2]/table/tbody/tr[2]/td[1]/div/label/span/input')
b = driver.find_element_by_css_selector("[class='ivu-checkbox-input']")
# 点击成功
b.click()
time.sleep(1)
c = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div/div/div[1]/button[5]/span')
c.click()
time.sleep(1)
d = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[2]/div/button[2]/span')
d.click()
time.sleep(2)



# print('关闭')
driver.quit()
print('<<<<<<<<<<<<<<<<<<<<<测试完成')
