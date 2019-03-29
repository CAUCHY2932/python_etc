import requests
from bs4 import BeautifulSoup
# from urllib.parse import quote
from urllib.parse import urlencode
import sys
from lxml import etree
from config import *
from requests.exceptions import ConnectionError
# client = pymongo.MongoClient(MONGO_URL, connect=False)
# db = client[MONGO_DB]
import pymongo
from multiprocessing import Pool

class Qichacha(object):
    def __init__(self):
        pass

    def get_page_index(self,offset,keyword):
        url='https://www.qichacha.com/search?key={keyword}#p:{offset}&'.format(keyword=keyword,offset=offset)
        
        Request_headers={
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'en-GB,en;q=0.5',
            'Cache-Control':'max-age=0',
            'Connection':'keep-alive',
            'Cookie':'UM_distinctid=1648246e3e2105-0f286da990ab8f-77256752-e1000-1648246e3e3398; CNZZDATA1254842228=1244370978-1531191327-https%253A%252F%252Fwww.baidu.com%252F%7C1531202479; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1531194042,1531204802,1531205674,1531207182; zg_did=%7B%22did%22%3A%20%221648246e8d516b-0371e8373d8f25-77256752-e1000-1648246e8d6d6%22%7D; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201531204802020%2C%22updated%22%3A%201531207181085%2C%22info%22%3A%201531194042592%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.baidu.com%22%2C%22cuid%22%3A%20%2206a8dc6ba11a66c6d46b58838cf2e7ae%22%7D; hasShow=1; _uab_collina=153119431866858685479222; PHPSESSID=tkpr2hukcmiscab8fumssquht6; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1531207182; acw_tc=AQAAADExS1W3dwAA9DiUtmrKklYEYCqV; _umdata=85957DF9A4B3B3E842A8332BD23FA48FC95A90703E91E47F3332796D13B36E2E77C3B8FF6DE6C244CD43AD3E795C914CDBDBE4360F720A87C3642A67715540D9',
            'Host':'www.qichacha.com',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'
        }
        try:
            response=requests.get(url,headers=Request_headers)
            if response.status_code == 200:
                response.encoding='utf-8'
                return response.text
            return None
        except ConnectionError:
            print('Error occurred')
            return None

    def parse_page_index(self,text):
        result=etree.HTML(text)
        tr_lst=result.xpath('/html/body/div/div/div/div/section/table/tbody/tr')
        for item in tr_lst:
            link=item.xpath('./td[2]/a/@href')[0]
            title=item.xpath('./td[2]/a/text()')[0]
            print(link,title)
            link_new='https://www.qichacha.com'+link
            yield link_new


    def get_page_detail(self,url):
        Request_headers={
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'en-GB,en;q=0.5',
            'Cache-Control':'max-age=0',
            'Connection':'keep-alive',
            'Cookie':'UM_distinctid=1648246e3e2105-0f286da990ab8f-77256752-e1000-1648246e3e3398; CNZZDATA1254842228=1244370978-1531191327-https%253A%252F%252Fwww.baidu.com%252F%7C1531202479; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1531194042,1531204802,1531205674,1531207182; zg_did=%7B%22did%22%3A%20%221648246e8d516b-0371e8373d8f25-77256752-e1000-1648246e8d6d6%22%7D; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201531204802020%2C%22updated%22%3A%201531207181085%2C%22info%22%3A%201531194042592%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.baidu.com%22%2C%22cuid%22%3A%20%2206a8dc6ba11a66c6d46b58838cf2e7ae%22%7D; hasShow=1; _uab_collina=153119431866858685479222; PHPSESSID=tkpr2hukcmiscab8fumssquht6; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1531207182; acw_tc=AQAAADExS1W3dwAA9DiUtmrKklYEYCqV; _umdata=85957DF9A4B3B3E842A8332BD23FA48FC95A90703E91E47F3332796D13B36E2E77C3B8FF6DE6C244CD43AD3E795C914CDBDBE4360F720A87C3642A67715540D9',
            'Host':'www.qichacha.com',
            'Upgrade-Insecure-Requests':'1',
            'Referer':'https://www.qichacha.com/search?key=%E6%88%90%E9%83%BD%E9%AB%98%E6%96%B0%E5%8C%BA',
            'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'
        }
        try:
            response=requests.get(url,headers=Request_headers)
            if response.status_code == 200:
                response.encoding='utf-8'
                return response.text
            return None
        except ConnectionError:
            print('Error occurred')
            return None

    def parse_page_detail(self,html):
        pass
    def turn_page(self):
        pass

    def save_to_mongo(self,result):
        if db[MONGO_TABLE].insert(result):
            print('Successfully Saved to Mongo', result)
            return True
        return False


    def main(self,offset):
        text = self.get_page_index(offset, KEYWORD)
        urls = self.parse_page_index(text)
        for url in urls:
            html = self.get_page_detail(url)
            print(html)
            # result = self.parse_page_detail(html, url)
            # if result: self.save_to_mongo(result)



        html=self.get_page_index('成都高新区',4)
        self.parse_page_index(html)
if __name__ == '__main__':
    
    qichacha=Qichacha()    
    qichacha.main()



