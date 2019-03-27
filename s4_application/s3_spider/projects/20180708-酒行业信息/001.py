# conding:utf-8
# time:20180706

import requests
from lxml import etree
from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import time
# from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import re


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
        # self.driver.close()
        return html



    def main(self):
        html=self.get_page_index()
        print(html)





if __name__ == '__main__':
    gs=Gongshang()
    gs.main()