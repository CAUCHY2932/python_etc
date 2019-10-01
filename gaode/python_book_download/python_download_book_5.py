# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/6/25 11:15
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
import time

import requests
from requests import RequestException
from lxml import etree


def get_book_url():
    url_list = ['http://www.allitebooks.org/page/{}/?s=python'.format(item) for item in range(1, 54)]
    return url_list


def get_book_detail_link(url):
    print('休息')
    time.sleep(3)
    try:
        resp = requests.get(url)
        return resp.text if resp.status_code == 200 else ''
    except RequestException as e:
        print('发生错误:{}'.format(e))
        return ''


def get_book_download_link(text):
    html = etree.HTML(text)

    res = html.xpath('//main[@id="main-content"]/div/article/div//h2[@class="entry-title"]/a/@href')
    print('当前爬取的链接是:\n{}'.format(res))
    return res
    # for item in res:
    #     print(item)


def get_download_link(item):
    # for item in res:
    print('--------------歇会---------------')
    time.sleep(5)
    # print(item)
    item = get_book_detail_link(item)
    html = etree.HTML(item)
    res = html.xpath('//span[@class="download-links"]/a/@href')
    print('book name is {}'.format(res))
    return res
    # print(res)
    pass


def download(item):
        # print('正在下载', item)
    try:
        resp = requests.get(item)
        if resp.status_code == 200:
            file_name = item.split('/')[-1]
            print('正在下载{}:\n'.format(file_name))
            with open('./new3/'+file_name, 'wb') as f:
                f.write(resp.content)
        time.sleep(3)
    except RequestException as e:
        print(e)
    pass


def go():
    url_list = get_book_url()
    for url in url_list:
        content_list = get_book_detail_link(url)
    # print(content_list)
    # for item in content_list:
    #     print(item)
    #     for item in content_list:
        res = get_book_download_link(content_list)
        for item3 in res:
            res2 = get_download_link(item3)
            # download(res)
            for item2 in res2:
                download(item2)
    # pass


if __name__ == '__main__':
    go()
    pass
