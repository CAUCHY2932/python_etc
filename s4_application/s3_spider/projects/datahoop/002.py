import re
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from pyquery import PyQuery as pq
# from config import *
# import pymongo
import time





# browser = webdriver.PhantomJS(service_args=SERVICE_ARGS)
browser = webdriver.Chrome()

wait = WebDriverWait(browser, 10)

browser.set_window_size(1400, 900)

url='http://ai.datahoop.cn/login.html'
username='cd013jiangliping'
password='CPDA1234'

def search():
    print('正在搜索')
    try:
        browser.get(url)
        input_usr = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#username'))
        )
        input_pwd = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#pwd'))
        )
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div > div > i')))
        for item in username:
            time.sleep(0.5)
            input_usr.send_keys(item)

        for item in password:
            time.sleep(0.5)
            input_pwd.send_keys(item)
        submit.click()
        browser.save_screenshot('1.png')
        # total = wait.until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.total')))
        # get_products()
        return total.text
        time.sleep(5)
        browser.quit()
    except TimeoutException:
        return search()



search()
