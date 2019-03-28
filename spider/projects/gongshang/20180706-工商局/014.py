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
        url = 'http://search.saic.gov.cn/'
        self.driver.get(url)
        self.driver.switch_to.frame('DataList')

        time.sleep(3)
        html=self.driver.page_source
        # self.driver.close()
        return html

    def parse_page_index(self,html):
        result=etree.HTML(html)
        lst=result.xpath('//*[@id="documentContainer"]/div[@class="row"]/li[@class="mc"]/div/a/@href')

        return lst

    def join_url(self,url):
        pattern=re.compile(r'../..(.*)')
        result=re.search(pattern,url).group(1)
        base_url='http://search.saic.gov.cn'
        url=base_url+result
        return url

    def get_page_detail(self,url):
        response = requests.get(url)
        response.encoding = 'utf-8'
        # print(response.text)
        return response.text

    def parse_page_detail(self,html):
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
        # print(info)


        result=etree.HTML(html)
        # title=result.xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div/p[1]/font/strong/text()')[0]
        content=result.xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div/p/text()')
        if len(content)!=0:
            print("1*"*100)
            return info,content
        else:
            content=result.xpath('/html/body/div[4]/div[2]/div[3]/div[1]/p/text()')
            if len(content)!=0:
                print("2*" * 100)
                print(content)

                return info,content
            else:
                content=result.xpath('/html/body/div[4]/div[2]/div[3]/div[1]/p/font/text()')
                if len(content)!=0:
                    print("3*" * 100)

                    return info,content
                else:
                    print("4*" * 100)
                    return info,[]


    def get_next_page(self):
        self.driver.find_element_by_xpath('//*[@id="list_navigator"]/span[3]/a').click()
        pass

    def main(self):
        html=self.get_page_index()
        for i in range(10):
            # time.sleep(5)
            # self.get_next_page()
            # self.driver.switch_to.frame('DataList')

            # print(html)
            lst=self.parse_page_index(html)
            for item in lst:
                item=self.join_url(item)
                print(item)
                html=self.get_page_detail(item)

                info,content=self.parse_page_detail(html)
                print(info)
                for item in content:
                    print(item)
            time.sleep(5)
            self.get_next_page()
            self.driver.switch_to.frame('DataList')



if __name__ == '__main__':
    gs=Gongshang()
    gs.main()