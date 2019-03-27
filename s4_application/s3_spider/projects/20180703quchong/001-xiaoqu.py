import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode
from lxml import etree
def get_page_index(base_url,keyword,cityNum):
    data={
        'wd':keyword,
        'c':cityNum,
    }
    headers={
        'User-Agent': 'Mozilla / 5.0(iPhone;CPU iPhone OS 11_0 like Mac OS X) AppleWebKit / 604.1.38(KHTML, like Gecko) Version / 11.0 Mobile / 15A372 Safari / 604.1',
    }
    url=base_url+urlencode(data)
    # print(url)
    response=requests.get(url)
    if response.status_code==200:
        print(response.text)
        return response.text
    return None

def parse_one_index(html):
    result=etree.HTML(html)

# def
def main():
    url='https://map.baidu.com/mobile/webapp/search/search/qt=s&'
    get_page_index(url,'小区',75)

if __name__ == '__main__':
    main()
