# coding:utf-8
import requests
from lxml import etree
import re
import os
from multiprocessing import Pool




def get_pg_src(url, text=True):
    resp = requests.get(url)
    try:
        if resp.status_code == 200:
            resp.encoding = resp.apparent_encoding
            return resp.text if text else resp.content
        return '' if text else b''
    except requests.exceptions.RequestException as e:
        return '' if text else b''


def parse_pg_src(raw_src):
    try:
        html = etree.HTML(raw_src)
        xp = html.xpath('//a[@class="ctrl download"]/@href')
        for item in xp:
            # print(item, type(item), str(item))
            yield str(item)
    except Exception as e:
        return []
    else:
        print('[success]-parse pg src success!')

def persistence(target_path,uri, content, order):
    try:
        if not os.path.exists(target_path):
            os.mkdir(target_path)
        filename = re.split(r'[?/]', uri)[1]
        with open(target_path+'/'+filename+'.jpg', mode='wb') as f:
            f.write(content)
    except Exception as e:
        print('[error]-', e)
    else:
        print('[success]-write %s file %s!'%(order, uri))

class Setting:
    host = 'https://bing.ioliu.cn/'
    url = 'https://bing.ioliu.cn/ranking'
    demo_pg_file = 'https://bing.ioliu.cn/ranking?p=1'
    demo_pg_link = 'https://bing.ioliu.cn/ranking?p=%s'
    page_footer = '//div[@class="page"]/span'
    target_path = '/Users/young/Desktop/pics'

def loop_call(func, pg_num):
    crawl_lst = [Setting.demo_pg_link%x for x in range(1, pg_num+1)]
    for item in crawl_lst:
        # print(item)
        func(item)
    pass

def get_page_num(raw_src):
    try:
        html = etree.HTML(raw_src)
        xp = html.xpath('//div[@class="page"]/span/text()')[0]
        b = xp.split('/')[1].strip()
        return b
    except Exception as e:
        return '[error]-%s'%e
    else:
        print('[success]-parse pg src success!')

def run_multiprocess_poll(func, pg_num):
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    crawl_lst = [Setting.demo_pg_link%x for x in range(1, int(pg_num)+1)]
    for i in crawl_lst:
        p.apply_async(func, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')


def crawl(url):
    raw_src = get_pg_src(url)
    # print(raw_src)
    file_lst=parse_pg_src(raw_src)
    order = 1
    for item in file_lst:
        suffix = item[1:]
        uri = Setting.host + item[1:]
        content_src = get_pg_src(Setting.host + item[1:], text=False)
        persistence(Setting.target_path,suffix, content_src, order)
        order += 1

def test_mkdir():
    filepath= Setting.target_path
    if not os.path.exists(filepath):
        os.mkdir(filepath)
        print('make filepath %s'%filepath)

if __name__ == "__main__":
    url = Setting.url
    raw_src = get_pg_src(url)
    pg_num = get_page_num(raw_src)
    run_multiprocess_poll(crawl,pg_num)
    pass
