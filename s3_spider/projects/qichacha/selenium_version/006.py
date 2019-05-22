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
import os
import re
import base64

# config_2
login_url='https://www.qichacha.com/user_login'
user_name='13458660542'
password='free134qaz'

class Qi(object):
    def __init__(self, *args, **kwargs):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(chrome_options=options)
        # os.mkdir('perpic')
        return None


    def login(self):

        self.driver.get(login_url)
        time.sleep(5)
        self.driver.find_element_by_id('normalLogin').click()# 点击正常登录
        time.sleep(5)

        for i in user_name:
            self.driver.find_element_by_id('nameNormal').send_keys(i)
            time.sleep(0.5)
        for p in password:
            self.driver.find_element_by_id('pwdNormal').send_keys(p)
            time.sleep(0.5)
        self.hold_drag()
        time.sleep(2)

        self.drag_down()
        time.sleep(2)
        self.pg_src=self.driver.page_source
        self.show_img()
        time.sleep(3)
        self.down_pic()
        # self.driver.save_screenshot('login_pic.png')
        self.driver.quit()
        # print(response)
        return None


    def hold_drag(self):
        action = ActionChains(self.driver)
        dragger = self.driver.find_element_by_id('nc_1_n1z') # 被拖拽元素

        action.click_and_hold(dragger).move_by_offset(348, 300).release().perform()
        # menu = self.driver.find_element_by_css_selector(".nav")
        # hidden_submenu = self.driver.find_element_by_css_selector(".nav #submenu1")

        # actions = ActionChains(self.driver)
        # actions.move_to_element(menu)
        # actions.click(hidden_submenu)
        # actions.perform()
        self.driver.save_screenshot('./perpic/slid.png')
        return None


    def drag_down(self):
        print('开始拖动啦')
        # js = "var q=document.body.scrollTop=100000"
        # js = "var q=document.body.scrollTop=55555"
        size='350'
        js="var q=document.documentElement.scrollTop="+size
        # driver.execute_script(js)

        self.driver.execute_script(js)
        time.sleep(3)
        self.driver.save_screenshot('./perpic/buttom.png')
        return None


    def show_img(self):
        pattern = re.compile('.*?<img src="data:image/jpg;base64,(.*?)" />',re.S)
        # ret=re.search(pattern,self.pg_src).group(1)
        # ret=re.findall(pattern,self.pg_src).group(4)
        # ret=re.search(pattern,self.pg_src)
        ret=re.findall(pattern,self.pg_src)



        # for item in ret:
        #     print(item)

        # print(ret[0])
        self.img_src=ret[0]
        return None



    def down_pic(self):
        imgdata=base64.b64decode(self.img_src)
        file=open('1.jpg','wb')
        file.write(imgdata)
        file.close()
        return None

    
    def main(self):
        # pass
        self.login()
        return None


if __name__ == '__main__':
    qi=Qi()
    qi.main()
    
