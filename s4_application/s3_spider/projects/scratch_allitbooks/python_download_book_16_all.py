# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/6/25 11:15
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
import time
import os
import requests
from requests import RequestException
from lxml import etree
import logging
import re
import sys
import config

keyword = config.KEYWORD
current_time = int(time.time())
# define the log file, file mode and logging level
# logging.basicConfig(filename='example2.log', filemode="w", level=logging.INFO)
logging.basicConfig(filename='{}-{}.log'.format(keyword, current_time), level = logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.debug('debug message')
logging.info('info message')
logging.warning('warning')


def http_help(url):
    try:
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}
        resp = requests.get(url, headers=headers, timeout=3)
        return resp.text if resp.status_code == 200 else ''
    except RequestException as e:
        print('[error]-{}'.format(e))
        return ''


def get_single_page_books(page, text):
    html = etree.HTML(text)
    try:
        res = html.xpath('//main[@id="main-content"]/div/article/div//h2[@class="entry-title"]/a/@href')
        print('[parsing]这是第{}页：\n[本页书籍的链接]-\n{}'.format(page, '\n'.join(res)))
        return res
    except Exception as e:
        print('[error]-', e)   
        return []


def get_single_book_link(page, item):
    item = http_help(item)
    html = etree.HTML(item)
    try:
        res = html.xpath('//span[@class="download-links"]/a/@href')
        print('[list]-这是第{}页：\n[versions]-\n{}'.format(page, '\n'.join(res)))
        return res
    except Exception as e:
        print('error:', e)
        return []

def download(page, item, folder_path):
    try:
        resp = requests.get(item)
        if resp.status_code == 200:
            file_name = item.split('/')[-1]
            print('[downloading]-这是第{}页：[正在下载]-{}'.format(page, file_name))
            with open(os.path.join(folder_path, file_name), 'wb') as f:
                f.write(resp.content)
            print('[downloaded]这是第{}页：[下载完成]-{}!'.format(page, file_name))
    except RequestException as e:
        print(e)

def get_pages(item):
    item = http_help(item)
    html = etree.HTML(item)
    try:
        res = html.xpath('//span[@class="pages"]/text()')[0]
        page = re.search(r'/(.*?)Pages', res).group(1).strip()
        page_num = int(page)
        print('[page]-共有{}页'.format(page_num))
        return page_num
    except IndexError:
        return 1
    except Exception as e:
        print('[error]-', e)
        return None


def go(folder_path, time):
    # if not os.path.exists(folder_path):
    #     os.mkdir(folder_path)
    origin_url = 'http://www.allitebooks.org/page/{}/?s={}'.format(1, keyword)
    pages = get_pages(origin_url)
    if not pages:
        return None
    for page in range(1, pages + 1):
        print('[pages]-这是第{}页-\n'.format(page))
        url = 'http://www.allitebooks.org/page/{}/?s={}'.format(page, keyword)
        content_list = http_help(url)
        res = get_single_page_books(page, content_list)
        # if len(res):
        #     res = [1,]
        for item3 in res:
            res2 = get_single_book_link(page, item3)
            for item2 in res2:
                print('[link]-link is {}'.format(item2))
                with open('./books_list_{}_{}.txt'.format(keyword, time),'a')as f:
                    f.write(item2+'\n')
                print('[success]-have write {} to txt'.format(item2))
#                download(page, item2, folder_path)


if __name__ == '__main__':
#    f_handler = open('out.log', 'w')
#    sys.stdout = f_handler
    folder_path = 'books-{}'.format(keyword)
    # sys.stdout = Loggers("./print_str.log")
    # print(current_time)
    go(folder_path, current_time)
