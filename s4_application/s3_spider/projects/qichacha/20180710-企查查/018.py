# !/usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
import requests
from selenium.webdriver.chrome.options import Options



# def get_source(url):
#     Request_headers = {
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#         'Accept-Encoding': 'gzip, deflate, br',
#         'Accept-Language': 'en-GB,en;q=0.5',
#         'Cache-Control': 'max-age=0',
#         'Connection': 'keep-alive',
#         'Cookie': 'UM_distinctid=1648246e3e2105-0f286da990ab8f-77256752-e1000-1648246e3e3398; CNZZDATA1254842228=1244370978-1531191327-https%253A%252F%252Fwww.baidu.com%252F%7C1531283479;zg_did=%7B%22did%22%3A%20%221648246e8d516b-0371e8373d8f25-77256752-e1000-1648246e8d6d6%22%7D;zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201531285720963%2C%22updated%22%3A%201531288555140%2C%22info%22%3A%201531194042592%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%2206a8dc6ba11a66c6d46b58838cf2e7ae%22%7D; _uab_collina=153119431866858685479222;_umdata=85957DF9A4B3B3E842A8332BD23FA48FC95A90703E91E47F3332796D13B36E2E77C3B8FF6DE6C244CD43AD3E795C914CDBDBE4360F720A87C3642A67715540D9; PHPSESSID=803obe1eqjt93q0ougkijv5lu1; acw_tc=AQAAAP0U0nhyYwYA9TiUtrZGujp7C7EL',
#         'Host': 'www.qichacha.com',
#         'Upgrade-Insecure-Requests': '1',
#         'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'
#     }
#     response=requests.get(url,headers=Request_headers)
#     print(response.status_code)
#     if response.status_code==200:
#         response.encoding='utf-8'
#         print(response.text)

#         return response.text
#     return None

def selenium_get_src(url):
    # 进入浏览器设置
    options = webdriver.ChromeOptions()
    # 设置中文
    # options.add_argument('lang=zh_CN.UTF-8')
    # options.add_argument('Accept-Encoding=gzip, deflate, br')
    # options.add_argument('Accept="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"')
    # options.add_argument('Accept-Language=en-GB,en;q=0.5')
    # options.add_argument('Cache-Control="max-age=0"')
    # options.add_argument('Connection="keep-alive"')
    # options.add_argument('Cookie="UM_distinctid=1648246e3e2105-0f286da990ab8f-77256752-e1000-1648246e3e3398; CNZZDATA1254842228=1244370978-1531191327-https%253A%252F%252Fwww.baidu.com%252F%7C1531283479;zg_did=%7B%22did%22%3A%20%221648246e8d516b-0371e8373d8f25-77256752-e1000-1648246e8d6d6%22%7D;zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201531285720963%2C%22updated%22%3A%201531288555140%2C%22info%22%3A%201531194042592%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%2206a8dc6ba11a66c6d46b58838cf2e7ae%22%7D; _uab_collina=153119431866858685479222;_umdata=85957DF9A4B3B3E842A8332BD23FA48FC95A90703E91E47F3332796D13B36E2E77C3B8FF6DE6C244CD43AD3E795C914CDBDBE4360F720A87C3642A67715540D9; PHPSESSID=803obe1eqjt93q0ougkijv5lu1; acw_tc=AQAAAP0U0nhyYwYA9TiUtrZGujp7C7EL"')
    # options.add_argument('Host="www.qichacha.com"')
    # options.add_argument('Upgrade-Insecure-Requests="1"')
    # options.add_argument('User-Agent= "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"')


    Request_headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-GB,en;q=0.5',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'UM_distinctid=1648246e3e2105-0f286da990ab8f-77256752-e1000-1648246e3e3398; CNZZDATA1254842228=1244370978-1531191327-https%253A%252F%252Fwww.baidu.com%252F%7C1531283479;zg_did=%7B%22did%22%3A%20%221648246e8d516b-0371e8373d8f25-77256752-e1000-1648246e8d6d6%22%7D;zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201531285720963%2C%22updated%22%3A%201531288555140%2C%22info%22%3A%201531194042592%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%2206a8dc6ba11a66c6d46b58838cf2e7ae%22%7D; _uab_collina=153119431866858685479222;_umdata=85957DF9A4B3B3E842A8332BD23FA48FC95A90703E91E47F3332796D13B36E2E77C3B8FF6DE6C244CD43AD3E795C914CDBDBE4360F720A87C3642A67715540D9; PHPSESSID=803obe1eqjt93q0ougkijv5lu1; acw_tc=AQAAAP0U0nhyYwYA9TiUtrZGujp7C7EL',
        'Host': 'www.qichacha.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'
    }
    # # 更换头部
    # options.add_argument('user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')
    browser = webdriver.Chrome(chrome_options=options)
    # url = "https://httpbin.org/get?show_env=1"

    browser.add_cookie(Request_headers)
    # browser.add_cookie({
    #     # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    #     # 'Accept-Encoding': 'gzip, deflate, br',
    #     # 'Accept-Language': 'en-GB,en;q=0.5',
    #     # 'Cache-Control': 'max-age=0',
    #     # 'Connection': 'keep-alive',
    #     'Cookie': 'UM_distinctid=1648246e3e2105-0f286da990ab8f-77256752-e1000-1648246e3e3398; CNZZDATA1254842228=1244370978-1531191327-https%253A%252F%252Fwww.baidu.com%252F%7C1531283479;zg_did=%7B%22did%22%3A%20%221648246e8d516b-0371e8373d8f25-77256752-e1000-1648246e8d6d6%22%7D;zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201531285720963%2C%22updated%22%3A%201531288555140%2C%22info%22%3A%201531194042592%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%2206a8dc6ba11a66c6d46b58838cf2e7ae%22%7D; _uab_collina=153119431866858685479222;_umdata=85957DF9A4B3B3E842A8332BD23FA48FC95A90703E91E47F3332796D13B36E2E77C3B8FF6DE6C244CD43AD3E795C914CDBDBE4360F720A87C3642A67715540D9; PHPSESSID=803obe1eqjt93q0ougkijv5lu1; acw_tc=AQAAAP0U0nhyYwYA9TiUtrZGujp7C7EL',
    #     # 'Host': 'www.qichacha.com',
    #     # 'Upgrade-Insecure-Requests': '1'
    #     # 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'
    #     })
        
    # browser.add_cookie({'UM_distinctid':'1648246e3e2105-0f286da990ab8f-77256752-e1000-1648246e3e3398', 
    #     'CNZZDATA1254842228':'1244370978-1531191327-https%253A%252F%252Fwww.baidu.com%252F%7C1531283479',
    #     'zg_did':'%7B%22did%22%3A%20%221648246e8d516b-0371e8373d8f25-77256752-e1000-1648246e8d6d6%22%7D',
    #     'zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f':'%7B%22sid%22%3A%201531285720963%2C%22updated%22%3A%201531288555140%2C%22info%22%3A%201531194042592%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%2206a8dc6ba11a66c6d46b58838cf2e7ae%22%7D', 
    #     '_uab_collina':'153119431866858685479222',
    #     '_umdata':'85957DF9A4B3B3E842A8332BD23FA48FC95A90703E91E47F3332796D13B36E2E77C3B8FF6DE6C244CD43AD3E795C914CDBDBE4360F720A87C3642A67715540D9', 
    #     'PHPSESSID':'803obe1eqjt93q0ougkijv5lu1', 
    #     'acw_tc':'AQAAAP0U0nhyYwYA9TiUtrZGujp7C7EL'})

    browser.get(url)
    # code=browser.status_code
    response=browser.page_source
    browser.quit()
    print(response)
    # print(response.status_code)
    # if code==200:
    #     # response.encoding='utf-8'
    #     print(response.text)

    #     return response.text
    return None
    

url='https://www.qichacha.com/search?key=%E6%88%90%E9%83%BD%E9%AB%98%E6%96%B0%E5%8C%BA#p:7'
# get_source(url)
selenium_get_src(url)