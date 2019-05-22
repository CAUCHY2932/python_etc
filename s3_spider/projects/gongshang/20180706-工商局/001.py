# conding:utf-8
# time:20180706

import requests
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# browser=webdriver.Chrome()


def search():
    browser = webdriver.PhantomJS()

    url = 'http://search.saic.gov.cn/'

    # browser.get('http://www.taobao.com')
    browser.get(url)

    # element = WebDriverWait(browser, 10).until(
    #     EC.presence_of_element_located((By.ID, "list_navigator"))
    # )
    time.sleep(3)
    browser.save_screenshot('2.png')
    html=browser.page_source
    browser.close()
    return html

def get_page_index():
    url = 'http://search.saic.gov.cn/'

    headers = {'Cookie': 'AD_RS_COOCIE=20111118',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'}
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    if response.status_code == 200:
        # print(response.text)
        return response.text
    # print('None')
    return None
def parse_page_index(html):
    result=etree.HTML(html)
    # lst=result.xpath('//*[@id="documentContainer"]/div[@class="row"]')

    lst=result.xpath('//*[@id="documentContainer"]/div[@class="row"]/li[@class="mc"]/div/a/@href')
    print(lst)
    for item in lst:
        print(item)


def main():
    # html=get_page_index()
    html=search()
    print(html)
    parse_page_index(html)

if __name__ == '__main__':
    main()