# !/usr/bin/python
# -*- coding: utf-8 -*-
# time:20180712-11:16

from selenium import webdriver
import requests
import time
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
# from config_2 import *

# config_2
login_url='https://www.qichacha.com/user_login'
user_name='13458660542'
password='free134qaz'

class Qi(object):
    def __init__(self, *args, **kwargs):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(chrome_options=options)


    def login(self):

        self.driver.get(login_url)
        time.sleep(5)
        self.driver.find_element_by_id('normalLogin').click()# 点击正常登录
        time.sleep(1)

        for i in user_name:
            self.driver.find_element_by_id('nameNormal').send_keys(i)
            time.sleep(0.5)
        for p in password:
            self.driver.find_element_by_id('pwdNormal').send_keys(p)
            time.sleep(0.5)
        self.hold_drag()
        time.sleep(3)


        # response=self.driver.page_source
        self.driver.save_screenshot('login_pic.png')
        self.driver.quit()
        # print(response)

    def hold_drag(self):
        action = ActionChains(self.driver)
        dragger = self.driver.find_element_by_id('nc_1_n1z') # 被拖拽元素

        action.click_and_hold(dragger).move_by_offset(400, 348).release().perform()
        # menu = self.driver.find_element_by_css_selector(".nav")
        # hidden_submenu = self.driver.find_element_by_css_selector(".nav #submenu1")

        # actions = ActionChains(self.driver)
        # actions.move_to_element(menu)
        # actions.click(hidden_submenu)
        # actions.perform()
    def main(self):
        # pass
        self.login()


if __name__ == '__main__':
    qi=Qi()
    qi.main()
    