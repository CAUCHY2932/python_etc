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



def get_page_index():
    url = 'http://search.saic.gov.cn/'
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(url)
    driver.switch_to.frame('DataList')

    time.sleep(3)
    html=driver.page_source
    driver.close()
    return html

def parse_page_index(html):
    result=etree.HTML(html)
    lst=result.xpath('//*[@id="documentContainer"]/div[@class="row"]/li[@class="mc"]/div/a/@href')

    return lst

def join_url(url):
    pattern=re.compile(r'../..(.*)')
    result=re.search(pattern,url).group(1)
    base_url='http://search.saic.gov.cn'
    url=base_url+result
    return url

def get_page_detail(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    # print(response.text)
    return response.text

def parse_page_detail(html):
    result=re.findall('.*class="Three_xilan01_02 Three_xilan01_0201">(.*?)</.*',html)

    result2=re.findall('.*class="Three_xilan01_0201">(.*?)</.*',html)

    info = {}

    info['索 引 号'] = result[0]
    info['主题分类'] = result[1]
    info['发布机构'] = result[2]
    info['发文日期'] = result[3]
    info['名    称'] = result2[0]
    info['文    号'] = result[4]
    info['主 题 词'] = result[5]
    info['体    裁'] = result[6]
    info['公开责任部门'] = result[7]
    info['公开类别'] = result[8]
    info['发布形式'] = result[9]
    info['备    注'] = result2[1]
    print(info)
def main():
    html=get_page_index()
    # print(html)
    lst=parse_page_index(html)
    for item in lst:
        item=join_url(item)
        html=get_page_detail(item)
        # print(html)
        parse_page_detail(html)
if __name__ == '__main__':
    main()