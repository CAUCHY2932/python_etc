# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/6/25 11:15
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
# import time
import os
import requests
from requests import RequestException
from lxml import etree
import logging

import sys

# define the log file, file mode and logging level
# logging.basicConfig(filename='example2.log', filemode="w", level=logging.INFO)
#       logging.basicConfig(filename='example6.log', level = logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#       logging.debug('debug message')
#       logging.info('info message')
#       logging.warning('warning')


def http_help(url):
    try:
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}
        resp = requests.get(url, headers=headers, timeout=3)
        return resp.text if resp.status_code == 200 else ''
    except RequestException as e:
        print('发生错误:{}'.format(e))
        return ''


def get_single_page_books(page, text):
    html = etree.HTML(text)
    res = html.xpath('//main[@id="main-content"]/div/article/div//h2[@class="entry-title"]/a/@href')
    print('这是第{}页：[本页书籍的链接]-\n{}'.format(page, '\n'.join(res)))
    return res


def get_single_book_link(page, item):
    item = http_help(item)
    html = etree.HTML(item)
    res = html.xpath('//span[@class="download-links"]/a/@href')
    print('这是第{}页：[这本书有以下几种版本]-\n{}'.format(page, '\n'.join(res)))
    return res


def download(page, item, folder_path):
    try:
        resp = requests.get(item)
        if resp.status_code == 200:
            file_name = item.split('/')[-1]
            print('这是第{}页：[正在下载]-{}'.format(page, file_name))
            with open(os.path.join(folder_path, file_name), 'wb') as f:
                f.write(resp.content)
            print('这是第{}页：[下载完成]-{}!'.format(page, file_name))
    except RequestException as e:
        print(e)


def go():
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    pages = 53
    for page in range(8, pages + 1):
        print('[这是第{}页]\n'.format(page))
        url = 'http://www.allitebooks.org/page/{}/?s=python'.format(page)
        content_list = http_help(url)
        res = get_single_page_books(page, content_list)
        for item3 in res:
            res2 = get_single_book_link(page, item3)
            for item2 in res2:
                download(page, item2, folder_path)


def down_from_file_list(item, folder_path):
    try:
        resp = requests.get(item)
        if resp.status_code==200:
            file_name = item.split('/')[-1]
            if os.path.exists(os.path.join(folder_path, file_name)):
                file_name = 'copy_' + file_name
                
            with open(os.path.join(folder_path, file_name), 'wb')as f:
                f.write(resp.content)
                return True
        return False
    except Exception as e:
        print(e)
        return False


def read_from_file(file_name):
    with open(file_name, 'r') as f:
        frl = f.readlines()
    return frl


if __name__ == '__main__':
#    f_handler = open('out.log', 'w')
#    sys.stdout = f_handler
    folder_path = 'mybook'
    # sys.stdout = Loggers("./print_str.log")
    # go()
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    
    file_list = read_from_file('./ebook_list.txt')
    dup_book_list = set()
    for i in file_list:
        print('[正在下载]-{}'.format(i))
        is_success_download = down_from_file_list(i, folder_path)
        if is_success_download:
            print('[成功下载]-{}'.format(i))
        else:
            print('[下载失败]-{}'.format(i))
            dup_book_list.add(i)
    while len(dup_book_list) != 0:
        link = dup_book_list.pop()
        print('[正在下载]-{}'.format(link))
        is_success_download = down_from_file_list(link, folder_path)
        if is_success_download:
            print('[成功下载]-{}'.format(link))
        else:
            print('[下载失败]-{}'.format(link))
            dup_book_list.add(link)
    print('-'*20+'下载完成'+'-'*20)
