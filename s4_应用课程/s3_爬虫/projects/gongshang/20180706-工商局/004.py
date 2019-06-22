# conding:utf-8
# time:20180706

import requests
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import re









def get_page_index():
    url = 'http://search.saic.gov.cn/'
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    # driver = webdriver.PhantomJS()# 这个路径就是你添加到PATH的路径

    driver.get(url)

    driver.switch_to.frame('DataList')
    # print(driver.page_source)
    # soup = BeautifulSoup(driver.page_source, "html.parser")
    # element = WebDriverWait(browser, 10).until(
    #     EC.presence_of_element_located((By.ID, "list_navigator"))
    # )
    time.sleep(3)
    # browser.save_screenshot('2.png')
    html=driver.page_source
    driver.close()
    return html

# def get_page_index2():
#     url = 'http://search.saic.gov.cn/'
#
#     headers = {'Cookie': 'AD_RS_COOCIE=20111118',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'}
#     response = requests.get(url, headers=headers)
#     response.encoding = 'utf-8'
#     if response.status_code == 200:
#         # print(response.text)
#         return response.text
#     # print('None')
#     return None
def parse_page_index(html):
    result=etree.HTML(html)
    # lst=result.xpath('//*[@id="documentContainer"]/div[@class="row"]')

    lst=result.xpath('//*[@id="documentContainer"]/div[@class="row"]/li[@class="mc"]/div/a/@href')
    # print(lst)
    # for item in lst:
    #     print(item)
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

def parse_page_detail2(html):
    result=etree.HTML(html)
    # info={}
    lst=result.xpath('/html/body/div/div/div/table/tbody/tr')
    print("*"*100)
    print(lst)
    print(len(lst))
    for item in lst:
        print(item)
        info = {}

        info['索 引 号']=item.xpath('./td/ul/li[2]/text()')[0]
        info['主题分类']=item.xpath('./td/ul/li[2]/text()')[0]
        info['发布机构']=item.xpath('./td/ul/li[2]/text()')[0]
        info['发文日期']=item.xpath('./td/ul/li[2]/text()')[0]
        info['名    称']=item.xpath('./td/ul/li/span[2]/text()')[0]
        info['文    号']=item.xpath('./td/ul/li[2]/text()')[0]
        info['主 题 词']=item.xpath('./td/ul/li[2]/text()')[0]
        info['体    裁']=item.xpath('./td/ul/li[2]/text()')[0]
        info['公开责任部门']=item.xpath('./td/ul/li[2]/text()')[0]
        info['公开类别']=item.xpath('./td/ul/li[2]/text()')[0]
        info['发布形式']=item.xpath('./td/ul/li[2]/text()')[0]
        info['备    注']=item.xpath('./td/ul/li/span[2]/text()')[0]
        print(info)
        print("&"*100)
# def parse_page_detail3(html):
#     soup=BeautifulSoup(html,'lxml')
#     # print(soup.find_all('li'))
#     print(soup.select())
def parse_page_detail(html):
    # cnt=0
    result=re.findall('.*class="Three_xilan01_02 Three_xilan01_0201">(.*?)</.*',html)
    # print(result)
    # for item in result:
    #     print(item)
    #     cnt+=1
    # print(cnt)
    result2=re.findall('.*class="Three_xilan01_0201">(.*?)</.*',html)
    # print(result2)

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