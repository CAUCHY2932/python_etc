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
from lxml import etree

# config_2
login_url='https://www.qichacha.com/user_login'
user_name='13458660542'
password='free134qaz'

class Qi(object):
    def __init__(self, *args, **kwargs):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(chrome_options=options)
        # os.mkdir('perpic')
        self.action = ActionChains(self.driver)

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
        time.sleep(2)
        self.get_word()
        self.click_pic()
        # self.driver.quit()
        self.driver.find_element_by_xpath('//*[@id="user_login_normal"]/button').click()
        
        return None


    def hold_drag(self):
        dragger = self.driver.find_element_by_id('nc_1_n1z') # 被拖拽元素

        self.action.click_and_hold(dragger).move_by_offset(348, 300).release().perform()
        self.driver.save_screenshot('./perpic/slid.png')
        return None


    def drag_down(self):
        size='350'
        js="var q=document.documentElement.scrollTop="+size
        self.driver.execute_script(js)
        time.sleep(3)
        self.driver.save_screenshot('./perpic/buttom.png')
        return None


    def show_img(self):
        pattern = re.compile('.*?<img src="data:image/jpg;base64,(.*?)" />',re.S)
        ret=re.findall(pattern,self.pg_src)
        self.img_src=ret[0]
        return None



    def down_pic(self):
        # 230pixels*230pixels
        # natural 200*200
        imgdata=base64.b64decode(self.img_src)
        file=open('1.jpg','wb')
        file.write(imgdata)
        file.close()
        return None

    def get_word(self):
        res=etree.HTML(self.pg_src)
        word=res.xpath('//*[@id="nc_1__scale_text"]/i/text()')[0]
        print(word)
        return None

    def click_pic(self):
        axies=input('请输入x坐标和y坐标，以空格作为间隔：').split()
        x=int(axies[0])
        y=int(axies[1])

        
        img_body = self.driver.find_element_by_xpath('//*[@id="nc_1_clickCaptcha"]/div[2]/img')
        self.action.move_to_element_with_offset(img_body,x,y).click().perform()

        return None

    
    def main(self):
        self.login()
        return None


if __name__ == '__main__':
    qi=Qi()
    qi.main()
    
