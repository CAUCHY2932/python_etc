import json
import os
from urllib.parse import urlencode
import pymongo
import requests
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError
import re
from multiprocessing import Pool
from hashlib import md5
from json.decoder import JSONDecodeError
# from config import *
from lxml import etree

from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options



class Gongshang(object):
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)


    def get_page_index(self):
        # url = 'http://search.saic.gov.cn/'
        url='http://www.gsxt.gov.cn/%7B6E05C133096330BEE5176B015A108CB644A53E650FEEA45490FAC032D39C90621EFFB54581EB70FEC7FD734AD1AD365C427AAE525FB35C9F73A772B15D9514C9146F146F14C9146FB21BE398E398E398458AFD3218F1C15D12325E054FD36D112B7014EC9BEC237EE2EED7B3E8A23E178B87BEE378F6CF54B5297216EE95EE95EE95-1531035286042%7D'
        self.driver.get(url)
        time.sleep(10)
        # self.driver.switch_to.frame('DataList')
        # js="var q=document.documentElement.scrollTop=10000"
        # driver_js.executeScript("window.scrollTo(0,document.body.scrollHeight)");
        # self.driver.execute_script(js)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

        time.sleep(5)
        html=self.driver.page_source
        self.driver.close()
        return html

    def save_to_mongo(self,result):
        if db[MONGO_TABLE].insert(result):
            print('Successfully Saved to Mongo', result)
            return True
        return False

    def parse_page_detail(self,html):
        result = etree.HTML(html)
        # 营业执照信息
        yyzz = result.xpath('//*[@id="primaryInfo"]//div[@class="overview"]')[0]
        # yyzz_table={}
        honest_code = yyzz.xpath('./dl[1]/dd/text()')[0].split()[0]
        name = yyzz.xpath('./dl[2]/dd/text()')[0].split()[0]
        type = yyzz.xpath('./dl[3]/dd/text()')[0].split()[0]
        legal_p = yyzz.xpath('./dl[4]/dd/text()')[0].split()[0]
        auth_money = yyzz.xpath('./dl[5]/dd/text()')[0].split()[0]
        bulid_date = yyzz.xpath('./dl[6]/dd/text()')[0].split()[0]
        time_from = yyzz.xpath('./dl[7]/dd/text()')[0].split()[0]
        time_to = yyzz.xpath('./dl[8]/dd/text()')[0].split()[0]
        auth_office = yyzz.xpath('./dl[9]/dd/text()')[0].split()[0]
        auth_time = yyzz.xpath('./dl[10]/dd/text()')[0].split()[0]
        auth_state = yyzz.xpath('./dl[11]/dd/text()')[0].split()
        addr = yyzz.xpath('./dl[12]/dd/text()')[0].split()[0]
        range_of_sale = yyzz.xpath('./dl[13]/dd/text()')[0].split()[0]
        yyzz_table = {
            "统一社会信用代码": honest_code,
            "企业名称": name,
            "类型": type,
            "法定代表人": legal_p,
            "注册资本": auth_money,
            "成立日期": bulid_date,
            "营业期限自": time_from,
            "营业期限至": time_to,
            "登记机关": auth_office,
            "核准日期": auth_time,
            "登记状态": auth_state,
            "住所": addr,
            "经营范围": range_of_sale,

        }
        return yyzz_table

    def get_holder_info(self,html):
        result = etree.HTML(html)
        holder_info=result.xpath('//*[@id="shareholderInfo"]/tbody/tr')
        holder_info_dict={}
        # for item in range(1,len(holder_info)+1):
        cnt = 1

        for item in holder_info:
            name=item.xpath('./td[2]/text()')[0]
            type_p=item.xpath('./td[3]/text()')
            type_p_str=''
            for i in type_p:
                type_p_str=type_p_str+i
            type_auth=item.xpath('./td[4]/text()')[0]
            num_auth=item.xpath('./td[5]/text()')[0]
            holder_info_dict[cnt]={
                "发起人名称":name,
                "发起人类型":type_p_str,
                "证件/证照类型":type_auth,
                "证照/证件号码":num_auth,
            }
            cnt+=1
        return holder_info_dict

    def get_personal_info(self,html):
        result=etree.HTML(html)
        personal_info=result.xpath('//*[@id="personInfo"]/ul/li')
        cnt=1
        personal_info_dict={}
        for item in personal_info:
            name=item.xpath('./a/div[@class="people-list-div list1"]/text()')
            name_str=''
            for i in name:
                name_str=name_str+i
                personal_info_dict[cnt]=name_str
                # personal_info_dict={
                #     cnt:name_str,
                # }
                cnt+=1
        return personal_info_dict










    def main(self):
        html=self.get_page_index()
        # print(html)
        dict_obj=self.parse_page_detail(html)
        print(dict_obj)
        holder_info_dict=self.get_holder_info(html)
        print(holder_info_dict)
        personal_info_dict=self.get_personal_info(html)
        print(personal_info_dict)























# client = pymongo.MongoClient(MONGO_URL, connect=False)
# db = client[MONGO_DB]




if __name__ == '__main__':
        gs = Gongshang()
        gs.main()