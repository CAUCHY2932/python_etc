# coding:utf-8

from selenium import webdriver
import time
import json

driver=webdriver.Chrome()
driver.get("https://mp.weixin.qq.com/")

driver.find_element_by_xpath('//*[@name="account"]').clear()
time.sleep(2)

driver.find_element_by_xpath('//*[@name="account"]').send_keys("")

driver.find_element_by_xpath('').clear()

driver.find_element_by_xpath('').send_keys()
time.sleep(2)

cookies=driver.get_cookie()
cookie={}

for item in cookies:
    cookie[item["name"]]=item

json.dumps(cookie)








