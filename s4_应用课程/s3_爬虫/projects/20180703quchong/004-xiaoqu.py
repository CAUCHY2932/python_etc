import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode
from lxml import etree
import re
import json
from multiprocessing import Pool
from requests.exceptions import  RequestException
from pyquery import PyQuery as pq
from selenium import webdriver



def get_page_index(base_url,keyword,cityNum,page_num):
    data={
        'wd':keyword,
        'c':cityNum,
        'pn':page_num,
        'rn':10,
    }
    headers={
        'User-Agent': 'Mozilla / 5.0(iPhone;CPU iPhone OS 11_0 like Mac OS X) AppleWebKit / 604.1.38(KHTML, like Gecko) Version / 11.0 Mobile / 15A372 Safari / 604.1',
    }
    url=base_url+urlencode(data)
    # print(url)
    response=requests.get(url,headers=headers)
    if response.status_code==200:
        # print(response.text)
        return response.text
    return None

def parse_page_index(html):
    result=etree.HTML(html)
    url_li=result.xpath('//*[@class="place-widget-placenewlist styleguide"]/ul/li/a/@href')
    # print(url_li)
    # return url_li

    for item in url_li:
        print(item)
def get_page_detail():
    base_url='/mobile/webapp/place/detail/qt=s&wd=%E5%B0%8F%E5%8C%BA&c=75&pn=0&rn=10&uid=d63a9773c9c1673f081cc7db/i=0&showall=1&pos=0&da_ref=listclk&da_qrtp=36&da_adtp=&da_log=&da_adquery=小区&da_adtitle=中海国际社区&da_adindus=房地产;住宅区&detail_from=list'
    # pass
    url='https://map.baidu.com'+base_url
    headers={
        'User-Agent': 'Mozilla / 5.0(iPhone;CPU iPhone OS 11_0 like Mac OS X) AppleWebKit / 604.1.38(KHTML, like Gecko) Version / 11.0 Mobile / 15A372 Safari / 604.1',
    }
    # url=base_url+urlencode(data)
    # print(url)
    response=requests.get(url,headers=headers)
    if response.status_code==200:
        # print(response.text)
        return response.text
    return None

def get_page_detail2():
    driver=webdriver.Chrome()

    base_url='/mobile/webapp/place/detail/qt=s&wd=%E5%B0%8F%E5%8C%BA&c=75&pn=0&rn=10&uid=d63a9773c9c1673f081cc7db/i=0&showall=1&pos=0&da_ref=listclk&da_qrtp=36&da_adtp=&da_log=&da_adquery=小区&da_adtitle=中海国际社区&da_adindus=房地产;住宅区&detail_from=list'
    # pass
    url='https://map.baidu.com'+base_url
    # headers={
    #     'User-Agent': 'Mozilla / 5.0(iPhone;CPU iPhone OS 11_0 like Mac OS X) AppleWebKit / 604.1.38(KHTML, like Gecko) Version / 11.0 Mobile / 15A372 Safari / 604.1',
    # }
    # url=base_url+urlencode(data)
    # print(url)
    # response=requests.get(url,headers=headers)
    driver.get(url)

    # if response.status_code==200:
    #     # print(response.text)
    #     return response.text
    # return None
def parse_page_detail(html):
    # html=pq(html)
    # print(html)
    result=etree.HTML(html)
    name=result.xpath('//*[@id="phoenix-header"]/div[1]/text()')

    addr=result.xpath('//*[@id="phoenix-header"]/div[2]/text()')
    abstract=result.xpath('//*[@id="phoenix_dom_2"]/div/div[2]')
    contents=result.xpath('//*[@id="summaryText"]/text()')
    return{
        'name':name,
        'addr':addr,
        'abstract':abstract,
        'contents':contents,
    }
    # u=result.xpath('')
def parse_page_detail2(html):
    # # html=pq(html)
    # # print(html)
    # # result=etree.HTML(html)
    # soup=BeautifulSoup(html,'lxml')
    # b=soup.find_all('#id="footer"')
    # # name=result.xpath('//*[@id="phoenix-header"]/div[1]/text()')
    # #
    # # addr=result.xpath('//*[@id="phoenix-header"]/div[2]/text()')
    # # abstract=result.xpath('//*[@id="phoenix_dom_2"]/div/div[2]')
    # # contents=result.xpath('//*[@id="summaryText"]/text()')
    # # return{
    # #     'name':name,
    # #     'addr':addr,
    # #     'abstract':abstract,
    # #     'contents':contents,
    # # }
    # print(b)
    pass
# def parse_page_detail3(html)
def main(offset):
    # url='https://map.baidu.com/mobile/webapp/search/search/qt=s&'
    url='https://map.baidu.com/mobile/webapp/place/list/qt=s&'
    html=get_page_index(url,'小区',75,offset)
    url_li=parse_page_index(html)

if __name__ == '__main__':
    # pool=Pool()
    # pool.map(main,[i for i in range(10)])
    # main(0)
    # html=get_page_detail()
    # # print(html)
    # # dict=parse_page_detail(html)
    # # print(dict)
    # parse_page_detail2(html)
    get_page_detail2()