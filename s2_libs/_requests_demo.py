# coding: utf-8
import requests
from bs4 import BeautifulSoup
from lxml import etree
from requests import RequestException
import json


def request_url(url):
    response=requests.get(url)
    if response.status_code==200:
        response.encoding=response.apparent_encoding
        print(response.text)


def get_page_source(url):
    # 获取源码
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            resp.encoding = resp.apparent_encoding
            return resp.text
        return ''
    except RequestException as e:
        print('error:', e)
        return ''


def parse_with_bs4(html_source):
    # 解析源码
    html=BeautifulSoup(html_source, 'lxml')
    # 创建css选择器
    items=html.select('script[type="text/javascript"]')
    for item in items:
        if "https://qr.alipay.com" in item.text:
            print(item)


def parse_with_xpath(html_source):
    # 解析源码
    s = etree.HTML(html_source)

    dictobj=s.xpath('//*[@id="J-barcode-container"]/canvas')

    with open("news.json", "a+", encoding='utf-8') as f:
        f.write(json.dumps(dictobj, ensure_ascii=False) + '\n')


def go():
    url = ''


if __name__ == "__main__":
    go()
