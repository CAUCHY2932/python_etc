# import json
# import os
# from urllib.parse import urlencode
import pymongo
import requests
# from bs4 import BeautifulSoup
# from requests.exceptions import ConnectionError
# import re
# from multiprocessing import Pool
# from hashlib import md5
# from json.decoder import JSONDecodeError
from config_new import *
from lxml import etree

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options


client = pymongo.MongoClient(MONGO_URL, connect=False)
db = client[MONGO_DB]

class Gongshang(object):
    def __init__(self):

        # ret = self.get_proxy()
        # print(ret)
        # ret2 = ret.split(':')
        # print(ret2[0])
        # # print(type(ret2[0]))
        # print(ret2[1])
        # # print(type(ret2[1]))
        # ip_addr = ret2[0]
        # ip_port = int(ret2[1])

        ip=self.get_proxy()
        print('已经切换到ip:',ip)


        chrome_options = Options()
        # chrome_options.add_argument('--headless')
        chrome_options.add_argument(('--proxy-server=http://' + ip))

        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        # self.wait = WebDriverWait(self.driver, 10)

    def get_page_index(self):
        # url = 'http://search.saic.gov.cn/'
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
        self.driver.quit()
        result = etree.HTML(html)

        return result

    def save_to_mongo(self,result):
        if db[MONGO_TABLE].insert(result):
            print('Successfully Saved to Mongo', result)
            return True
        return False

    def get_proxy(self):
        # return requests.get('http://123.207.35.36:5010/get/').content
        # return requests.get("http://127.0.0.1:5010/get/").content
        return requests.get("http://127.0.0.1:5010/get/").text

    def parse_page_detail(self,result):
        # 营业执照信息
        try:
            yyzz = result.xpath('//*[@id="primaryInfo"]//div[@class="overview"]')[0]
            # yyzz_table={}
            honest_code = yyzz.xpath('./dl[1]/dd/text()')[0].split()[0]
            name = yyzz.xpath('./dl[2]/dd/text()')[0].split()[0]
            type = yyzz.xpath('./dl[3]/dd/text()')[0].split()[0]
            legal_p = yyzz.xpath('./dl[4]/dd/text()')[0].split()[0]
            auth_money = yyzz.xpath('./dl[5]/dd/text()')[0].split()[0]
            bulid_date = yyzz.xpath('./dl[6]/dd/text()')[0].split()[0]
            time_from = yyzz.xpath('./dl[7]/dd/text()')[0].split()[0]
            # time_to = yyzz.xpath('./dl[8]/dd/text()')[0].split()[0]
            time_to = yyzz.xpath('./dl[8]/dd/text()')[0].split()

            auth_office = yyzz.xpath('./dl[9]/dd/text()')[0].split()[0]
            auth_time = yyzz.xpath('./dl[10]/dd/text()')[0].split()[0]
            auth_state = yyzz.xpath('./dl[11]/dd/text()')[0].split()[0]
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
        except Exception as e:
            yyzz_table={}
            print('抓取营业执照信息出错',e)
        finally:
            return yyzz_table

    def get_holder_info(self,result):
        # 发起人及出资信息
        try:

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
                holder_info_dict[str(cnt)]={
                    "发起人名称":name,
                    "发起人类型":type_p_str,
                    "证件/证照类型":type_auth,
                    "证照/证件号码":num_auth,
                }
                cnt+=1
        except Exception as e:
            holder_info_dict={}
            print('抓取发起人及出资信息出错',e)
        finally:
            return holder_info_dict

    def get_personal_info(self,result):
        # 主要人员信息
        try:
            personal_info=result.xpath('//*[@id="personInfo"]/ul/li')
            cnt=1
            personal_info_dict={}
            for item in personal_info:
                name=item.xpath('./a/div[1]/text()')
                name_str=''
                for i in name:
                    name_str=name_str+i
                personal_info_dict[str(cnt)]=name_str
                cnt+=1
        except Exception as e:
            personal_info_dict = {}
            print('抓取主要人员信息出错', e)
        finally:
            return personal_info_dict

    def get_branchGroup(self,result):
        # 分支机构信息
        try:
            branchGroup_info=result.xpath('//div[@id="branchGroupInfo"]/ul/li[@class="branchInfo-list"]')
            cnt=1
            branchGroup_dict={}
            for item in branchGroup_info:
                title=item.xpath('./a/div[1]/text()')[0]
                auth_num=item.xpath('./a/span/span/text()')[0]
                branchGroup_dict[str(cnt)]={
                    "分支机构名":title,
                    "统一社会信用代码/注册号:":auth_num,

                }
                cnt+=1
        except Exception as e:
            branchGroup_dict = {}
            print('抓取分支机构信息出错', e)
        finally:
            return branchGroup_dict

    def get_wrap_stock(self,result):
        # 股权出质登记信息
        try:
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


                wrap_stock_dict[str(cnt)]={
                    "登记编号":auth_num,
                    "出质人":wrap_p,
                    "证照/证件号码":cert_num,
                    "出质股权数额":wrap_mount,
                    "质权人":auth_p,
                    "股权出质设立登记日期":wrap_stock_date,
                    "状态":state,

                }
                cnt+=1
        except Exception as e:
            wrap_stock_dict = {}
            print('抓取股权出质登记信息出错', e)
        finally:
            return wrap_stock_dict




    def get_wrap_assist(self,result):
        # 司法协助信息
        try:
            wrap_assist_info = result.xpath('//div[@id="wrap-assist"]//div//tbody/tr')
            cnt = 1
            wrap_assist_dict = {}
            for item in wrap_assist_info:
                exe_p = item.xpath('./td[2]/text()')[0]
                stock_mount = item.xpath('./td[3]/text()')[0]
                exe_office = item.xpath('./td[4]/text()')[0]
                exe_code = item.xpath('./td[5]/text()')[0]
                state = item.xpath('./td[6]/span/text()')[0]

                wrap_assist_dict[str(cnt)] = {
                    "被执行人": exe_p,
                    "股权数额": stock_mount,
                    "执行法院": exe_office,
                    "执行通知书文号": exe_code,
                    "类型|状态": state,

                }
                cnt += 1
        except Exception as e:
            wrap_assist_dict = {}
            print('抓取司法协助信息出错', e)
        finally:
            return wrap_assist_dict

    def get_wrap_annualreport(self,result):
        # 企业年报信息
        try:
            wrap_annualreport_info = result.xpath('//div[@id="wrap-annualreport"]//div//tbody/tr')
            cnt = 1
            wrap_annualreport_dict = {}
            for item in wrap_annualreport_info:
                report_year = item.xpath('./td[2]/text()')[0]
                notice_date = item.xpath('./td[3]/text()')[0]
                # exe_office = item.xpath('./td[4]/text()')
                # exe_code = item.xpath('./td[5]/text()')
                # state = item.xpath('./td[6]/text()')

                wrap_annualreport_dict[str(cnt)] = {
                    "报送年度": report_year,
                    "公示日期": notice_date,
                    # "执行法院": exe_office,
                    # "执行通知书文号": exe_code,
                    # "类型|状态": state,

                }
                cnt += 1
        except Exception as e:
            wrap_annualreport_dict = {}
            print('抓取企业年报信息出错',e)
        finally:
            return wrap_annualreport_dict

    def get_wrap_instant(self,result):
        # 股东及出资信息
        try:
            wrap_instant_info = result.xpath('//div[@id="wrap-instant"]//div[@class="row"]//table[@id="needPaging_stock"]/tbody/tr')
            cnt = 1
            wrap_instant_dict = {}
            for item in wrap_instant_info:
                stock_p = item.xpath('./td[1]/text()')[0]
                should_mount = item.xpath('./td[2]/text()')[0]
                real_mount = item.xpath('./td[3]/text()')[0]
                # exe_code = item.xpath('./td[5]/text()')
                # state = item.xpath('./td[6]/text()')

                wrap_instant_dict[str(cnt)] = {
                    "股东": stock_p,
                    "认缴金额": should_mount,
                    "实缴金额": real_mount,
                    # "执行通知书文号": exe_code,
                    # "类型|状态": state,

                }
                cnt += 1
        except Exception as e:
            wrap_instant_dict = {}
            print('抓取股东及出资信息出错', e)
        finally:
            return wrap_instant_dict


    def main(self):


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

        data_dict={
            "营业执照信息":dict_obj,
            "发起人及出资信息":holder_info_dict,
            "主要人员信息":personal_info_dict,
            "分支机构信息":branchGroup_dict,
            "股权出质登记信息":wrap_stock,
            "司法协助信息":wrap_assist,
            "企业年报信息":wrap_annualreport,
            "股东及出资信息":wrap_instant,

        }
        self.save_to_mongo(data_dict)







if __name__ == '__main__':
        gs = Gongshang()
        gs.main()