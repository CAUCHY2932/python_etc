import requests
import os
from hashlib import md5
from urllib.parse import urlencode
from requests.exceptions import RequestException
import json
from bs4 import BeautifulSoup
import pymongo
from config import *
import re
from multiprocessing import Pool


client = pymongo.MongoClient(MONGO_URL, connect=False)
db = client[MONGO_DB]


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
        'user-agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 67.0.3396.62 Safari / 537.36'
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

def parse_page_detail(html,url):
    soup=BeautifulSoup(html,'lxml')
    title=soup.select('title')[0].get_text()
    # print(title)
    image_pattern=re.compile('JSON.parse\("(.*?)"\)',re.S)
    result=re.search(image_pattern,html)
    if result:
        # print(result.group(1))
        data=json.loads(result.group(1).replace('\\',''))
        if data and "sub_images" in data.keys():
            sub_images=data.get("sub_images")
            # print(sub_images)
            images=[item.get('url') for item in sub_images]
            for image in images:
                download_image(image)
            # print(images)
            return {
                "title":title,
                "url": url,
                "images":images,
            }

def download_image(url):
    print('downloading ',url)
    headers={
        'user-agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 67.0.3396.62 Safari / 537.36'
    }
    try:
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            response.encoding='utf-8'
            save_image(response.content)
            # return response.text
        return None
    except RequestException:
        print('请求图片出错')
        return None
# def save_image(content):
#     file_path='{0}/{1}.{2}'.format(os.getcwd(),md5(content).hexdigest,'jpg')
#     with open(file_path,'wb') as f:
#         f.write(content)

def save_image(content):
    file_path = '{0}/{1}.{2}'.format(os.getcwd(), md5(content).hexdigest(), 'jpg')
    print(file_path)
    if not os.path.exists(file_path):
        with open(file_path, 'wb') as f:
            f.write(content)
            f.close()

def save_to_mongo(result):
    if db[MONGO_TABLE].insert(result):
        print('Successfully Saved to Mongo', result)
        return True
    return False
def main(offset):
    html=get_one_page(offset,KEYWORD)
    # print(html)
    for url in parse_page_index(html):
        # print(url)
        html=get_page_detail(url)
        # print(html)
        if html:
            result=parse_page_detail(html,url)
            # print(result)
            if result:
                save_to_mongo(result)
if __name__ == "__main__":
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join()
