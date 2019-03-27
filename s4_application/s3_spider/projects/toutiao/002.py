import requests
from urllib.parse import urlencode
from requests.exceptions import RequestException
import json
from bs4 import BeautifulSoup
import re
def get_one_page(offset,keyword):
    data={
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': 20,
        'cur_tab': 1,
        'from': 'search_tab',

    }
    headers={
        'user - agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 67.0.3396.62 Safari / 537.36'
    }
    url='https://www.toutiao.com/search_content/?'+urlencode(data)
    # print(url)
    try:
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            response.encoding='utf-8'
            return response.text
        return None
    except RequestException:
        print('请求索引页出错')
        return None

def parse_page_index(html):
    data=json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')

def get_page_detail(url):
    headers={
        'user-agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 67.0.3396.62 Safari / 537.36'
    }
    try:
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            response.encoding='utf-8'
            return response.text
        return None
    except RequestException:
        print('请求详情页出错')
        return None

def parse_page_detail(html):
    soup=BeautifulSoup(html,'lxml')
    title=soup.select('title')[0].get_text()
    print(title)
    # image_pattern=re.compile('')

def main():
    html=get_one_page(0,'街拍')
    # print(html)
    for url in parse_page_index(html):
        print(url)
        html=get_page_detail(url)
        print(html)
        if html:
            parse_page_detail(html)
def test_():
    url='https://www.toutiao.com/a6572842651014398468/'
    headers = {
        'cookie': 'tt_webid = 6572875848323712520;tt_webid = 6572875848323712520;WEATHER_CITY = % E5 % 8C % 97 % E4 % BA % AC;UM_distinctid = 16450fa1d5f112 - 098a8439ca2a4b - 5e4b2519 - e1000 - 16450fa1d606fa;tt_webid = 6572875848323712520;csrftoken = 40d1afe00bccf68320887d51daeab156;sso_login_status = 0;CNZZDATA1259612802 = 1322280054 - 1530362654 - % 7C1530411254;__tasessionId = z1ypiwo4z1530413491561',
        'user - agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 67.0.3396.62 Safari / 537.36'
    }
    # cookies={}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            response.encoding = 'utf-8'
            return response.text
        return None
    except RequestException:
        print('请求详情页出错')
        return None
if __name__ == "__main__":
    main()
    # test_()
