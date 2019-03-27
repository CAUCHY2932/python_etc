# import json
# import os
# from urllib.parse import urlencode
# import pymongo
# import requests
# from bs4 import BeautifulSoup
# from requests.exceptions import ConnectionError
# import re
# from multiprocessing import Pool
# from hashlib import md5
# from json.decoder import JSONDecodeError
# # from config import *
from lxml import etree

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options


class Gongshang(object):
    def __init__(self):
        chrome_options = Options()
        # chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        # self.wait = WebDriverWait(self.driver, 10)

    def get_page_index(self):
        # url = 'http://search.saic.gov.cn/'
        url='http://www.gsxt.gov.cn/%' \
            '7B6E05C133096330BEE5176B015' \
            'A108CB644A53E650FEEA45490FAC032' \
            'D39C90621EFFB54581EB70FEC7FD734AD1A' \
            'D365C427AAE525FB35C9F73A772B15D9514C9146' \
            'F146F14C9146FB21BE398E398E398458AFD3218F1C15' \
            'D12325E054FD36D112B7014EC9BEC237EE2EED7B3E8A23E178B87' \
            'BEE378F6CF54B5297216EE95EE95EE95-1531035286042%7D'
        self.driver.get(url)
        time.sleep(15)
        # input = self.wait.until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, '#btn_print'))
        # )
        # self.driver.switch_to.frame('DataList')
        # js="var q=document.documentElement.scrollTop=10000"
        # driver_js.executeScript("window.scrollTo(0,document.body.scrollHeight)");
        # self.driver.execute_script(js)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        html=self.driver.page_source
        self.driver.close()
        return html

    # def save_to_mongo(self,result):
    #     if db[MONGO_TABLE].insert(result):
    #         print('Successfully Saved to Mongo', result)
    #         return True
    #     return False

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
            name=item.xpath('./a/div[1]/text()')
            name_str=''
            for i in name:
                name_str=name_str+i
            personal_info_dict[cnt]=name_str
            cnt+=1
        return personal_info_dict

    def get_branchGroup(self,html):
        result=etree.HTML(html)
        branchGroup_info=result.xpath('//div[@id="branchGroupInfo"]/ul/li[@class="branchInfo-list"]')
        cnt=1
        branchGroup_dict={}
        for item in branchGroup_info:
            title=item.xpath('./a/div[1]/text()')[0]
            auth_num=item.xpath('./a/span/span/text()')[0]
            branchGroup_dict[cnt]={
                "分支机构名":title,
                "统一社会信用代码/注册号:":auth_num,

            }
            cnt+=1
        return branchGroup_dict

    def get_wrap_stock(self,html):
        result=etree.HTML(html)
        wrap_stock_info=result.xpath('//*[@id="wrap-stock"]//tbody/tr//tbody/tr')
        cnt=1
        wrap_stock_dict={}
        for item in wrap_stock_info:
            auth_num=item.xpath('./td[2]/text()')[0]
            wrap_p=item.xpath('./td[3]/text()')[0]
            cert_num=item.xpath('./td[4]/text()')[0]
            wrap_mount=item.xpath('./td[5]/text()')[0]
            auth_p=item.xpath('./td[6]/text()')[0]
            wrap_stock_date=item.xpath('./td[8]/text()')[0]
            state=item.xpath('./td[9]/text()')[0]


            wrap_stock_dict[cnt]={
                "登记编号":auth_num,
                "出质人":wrap_p,
                "证照/证件号码":cert_num,
                "出质股权数额":wrap_mount,
                "质权人":auth_p,
                "股权出质设立登记日期":wrap_stock_date,
                "状态":state,

            }
            cnt+=1
        return wrap_stock_dict




    def get_wrap_assist(self,html):

        result = etree.HTML(html)
        wrap_assist_info = result.xpath('//div[@id="wrap-assist"]//div//tbody/tr')
        cnt = 1
        wrap_assist_dict = {}
        for item in wrap_assist_info:
            exe_p = item.xpath('./td[2]/text()')[0]
            stock_mount = item.xpath('./td[3]/text()')[0]
            exe_office = item.xpath('./td[4]/text()')[0]
            exe_code = item.xpath('./td[5]/text()')[0]
            state = item.xpath('./td[6]/span/text()')[0]

            wrap_assist_dict[cnt] = {
                "被执行人": exe_p,
                "股权数额": stock_mount,
                "执行法院": exe_office,
                "执行通知书文号": exe_code,
                "类型|状态": state,

            }
            cnt += 1
        return wrap_assist_dict

    def get_wrap_annualreport(self,html):

        result = etree.HTML(html)
        wrap_annualreport_info = result.xpath('//div[@id="wrap-annualreport"]//div//tbody/tr')
        cnt = 1
        wrap_annualreport_dict = {}
        for item in wrap_annualreport_info:
            report_year = item.xpath('./td[2]/text()')[0]
            notice_date = item.xpath('./td[3]/text()')[0]
            # exe_office = item.xpath('./td[4]/text()')
            # exe_code = item.xpath('./td[5]/text()')
            # state = item.xpath('./td[6]/text()')

            wrap_annualreport_dict[cnt] = {
                "报送年度": report_year,
                "公示日期": notice_date,
                # "执行法院": exe_office,
                # "执行通知书文号": exe_code,
                # "类型|状态": state,

            }
            cnt += 1
        return wrap_annualreport_dict

    def get_wrap_instant(self,html):

        result = etree.HTML(html)
        wrap_instant_info = result.xpath('//div[@id="wrap-instant"]//div[@class="row"]//table[@id="needPaging_stock"]/tbody/tr')
        cnt = 1
        wrap_instant_dict = {}
        for item in wrap_instant_info:
            stock_p = item.xpath('./td[1]/text()')[0]
            should_mount = item.xpath('./td[2]/text()')[0]
            real_mount = item.xpath('./td[3]/text()')[0]
            # exe_code = item.xpath('./td[5]/text()')
            # state = item.xpath('./td[6]/text()')

            wrap_instant_dict[cnt] = {
                "股东": stock_p,
                "认缴金额": should_mount,
                "实缴金额": real_mount,
                # "执行通知书文号": exe_code,
                # "类型|状态": state,

            }
            cnt += 1
        return wrap_instant_dict


    def main(self):

        # client = pymongo.MongoClient(MONGO_URL, connect=False)
        # db = client[MONGO_DB]

        html=self.get_page_index()
        print(html)

        dict_obj=self.parse_page_detail(html)
        print('营业执照信息')
        print(dict_obj)

        holder_info_dict=self.get_holder_info(html)
        print('发起人及出资信息')
        print(holder_info_dict)

        personal_info_dict=self.get_personal_info(html)
        print('主要人员信息')
        print(personal_info_dict)

        branchGroup_dict=self.get_branchGroup(html)
        print('分支机构信息')
        print(branchGroup_dict)

        wrap_stock=self.get_wrap_stock(html)
        print('股权出质登记信息')
        print(wrap_stock)

        wrap_assist=self.get_wrap_assist(html)
        print('司法协助信息')
        print(wrap_assist)

        wrap_annualreport=self.get_wrap_annualreport(html)
        print('企业年报信息')
        print(wrap_annualreport)

        wrap_instant=self.get_wrap_instant(html)
        print('股东及出资信息')
        print(wrap_instant)







if __name__ == '__main__':
        gs = Gongshang()
        gs.main()