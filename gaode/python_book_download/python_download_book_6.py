# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/6/25 11:15
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
# import time

import requests
from requests import RequestException
from lxml import etree


def get_book_url():
    url_list = ['http://www.allitebooks.org/page/{}/?s=python'.format(item) for item in range(1, 54)]
    return url_list


# headers = {'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
#                'Accept - Encoding':'gzip, deflate',
#                'Accept-Language':'zh-Hans-CN, zh-Hans; q=0.5',
#                'Connection':'Keep-Alive',
#                'Host':'zhannei.baidu.com',
#                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}
# r = requests.get('http://zhannei.baidu.com/cse/search', params=keyword, headers=headers, timeout=3)


def get_book_detail_link(url):
    print('-------------休息-------------------')
    # time.sleep(3)
    try:
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}
        resp = requests.get(url, headers=headers, timeout=3)
        return resp.text if resp.status_code == 200 else ''
    except RequestException as e:
        print('发生错误:{}'.format(e))
        return ''


def get_book_download_link(text):
    html = etree.HTML(text)

    res = html.xpath('//main[@id="main-content"]/div/article/div//h2[@class="entry-title"]/a/@href')
    print('[书的链接]\n{}'.format(res))
    return res


def get_download_link(item):
    item = get_book_detail_link(item)
    html = etree.HTML(item)
    res = html.xpath('//span[@class="download-links"]/a/@href')
    print('[书的列表] {}'.format(res))
    return res


def download(item):
    try:
        resp = requests.get(item)
        if resp.status_code == 200:
            file_name = item.split('/')[-1]
            print('[正在下载]-{}:\n'.format(file_name))
            with open('./n4/'+file_name, 'wb') as f:
                f.write(resp.content)
    except RequestException as e:
        print(e)


def go():
    url_list = get_book_url()
    for url in url_list:
        content_list = get_book_detail_link(url)
        res = get_book_download_link(content_list)
        for item3 in res:
            res2 = get_download_link(item3)
            for item2 in res2:
                download(item2)


if __name__ == '__main__':
    go()
    pass
