import requests
from bs4 import BeautifulSoup
# from urllib.parse import quote
from urllib.parse import urlencode
import sys
from lxml import etree

class Qichacha(object):
    def __init__(self,keyword):
        data={
            'key':keyword,
        }
        url='https://www.qichacha.com/search?'+urlencode(data)
        # url2='https://www.qichacha.com/search?key={}'.format(keyword)
        # print(url,url2)
        # print(url2)
        # print(urlencode(keyword))
        print(url)
        pass

    def get_page_index(self):
        pass

    def get_page_detail(self):
        pass

    def main(self):
        pass

if __name__ == '__main__':
    qichacha=Qichacha('成都高新区')    




