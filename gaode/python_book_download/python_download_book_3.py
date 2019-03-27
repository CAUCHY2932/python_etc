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


# 貌似yield出现了问题


def get_book_url():
    url_list = ['http://www.allitebooks.org/page/{}/?s=python'.format(item) for item in range(1, 54)]
    return url_list


def get_book_detail_link(url_list):
    for url in url_list:
        try:
            resp = requests.get(url)
            yield resp.text if resp.status_code == 200 else ''
        except RequestException as e:
            print('发生错误:{}'.format(e))
            yield ''


def get_book_download_link(text):
    html = etree.HTML(text)

    res = html.xpath('//main[@id="main-content"]/div/article/div//h2[@class="entry-title"]/a/@href')
    print('当前爬取的链接是:\n{}'.format(res))
    return res
    # for item in res:
    #     print(item)


def get_download_link(res):
    for item in get_book_detail_link(res):
        # print(item)
        html = etree.HTML(item)
        res = html.xpath('//span[@class="download-links"]/a/@href')
        print(res)
        return res
        # print(res)
        pass


def download(res_list):
    for item in res_list:
        print('正在下载', item)
        try:
            resp = requests.get(item)
            if resp.status_code == 200:
                file_name = item.split('/')[-1]
                print('正在下载{}:\n'.format(file_name))
                with open(file_name, 'wb') as f:
                    f.write(resp.content)
            time.sleep(3)
        except RequestException as e:
            print(e)
    pass


def go():
    url_list = get_book_url()
    content_list = get_book_detail_link(url_list)
    # print(content_list)
    # for item in content_list:
    #     print(item)
    for item in content_list:
        res = get_book_download_link(item)
        res = get_download_link(res)
        download(res)
        # for item2 in res:
        #     download(item2)
    # pass


if __name__ == '__main__':
    go()
    pass
