# -*- coding:utf-8 -*-
"""
    :DATE: 2019-06-27 10:38
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
    :author: young
"""
# https://www.cnblogs.com/yongjieShi/p/9599015.html
# https://blog.csdn.net/zx8167107/article/details/81083249
# https://www.baidu.com/s?ie=UTF-8&wd=python%E5%A4%9A%E7%BA%BF%E7%A8%8B%E5%A4%84%E7%90%86%E6%96%87%E4%BB%B6
# https://www.jianshu.com/p/7665545c970b
# https://www.cnblogs.com/freeman818/p/7154089.html
import pandas as pd
import requests
import json
import config
from multiprocessing import Pool
import time
import os
# from config import KEY_1
# from ... import config.KEY_1 as


def request_from_gaode(addr_str):
    payload = {
        "key": config.KEY_1,
        "output": "json",
        "address": addr_str}
    base_gaode_url = config.BASE_GAODE_URL
    resp = requests.get(base_gaode_url, payload)
    return resp.text if resp.status_code == 200 else "{}"


def package_data(addr):
    try:
        print('[crawl]-{}-{}'.format(os.getpid(), addr))
        addr = request_from_gaode(addr)
        addr_json = json.loads(addr)
        if addr_json["status"] == "1":
            province = addr_json["geocodes"][0]["province"]
            city = addr_json["geocodes"][0]["city"]
            district = addr_json["geocodes"][0]["district"]
            return province, city, district
        print('[error]-{}-request no respone'.format(os.getpid()))
        return "", "", ""
    except Exception as e:
        print('[error]-{}-{}'.format(os.getpid(), e))
        return "", "", ""


def new_process(chunk):
    processd = [package_data(x) for x in chunk['宴会地址']]
    # processd = list(map(package_data, chunk['宴会地址']))
    # chunk['province'], chunk['city'], chunk['district'] = [x[0] for x in processd], \
    #                                                       [x[1] for x in processd], \
    #                                                       [x[2] for x in processd]

    chunk['province'], chunk['city'], chunk['district'] = list(zip(*processd))

    csv_file_name = './{}.csv'.format(int(time.time()))
    # time.sleep(3)
    chunk.to_csv(csv_file_name, index=False, mode='a+')
    print('[success]-{}-gen-{}'.format(os.getpid(), csv_file_name))


def start(file_name):
    # header = None，会指定第一行为数据
    # 默认第一行为列名
    # for chunk in pd.read_csv(file_name, chunksize=1000):
    #     new_process(chunk)
    print('[start]'+'-'*15)
    t_start = time.time()
    pool = Pool(config.PROCESS_NUM)
    group = (chunk for chunk in pd.read_csv(file_name, chunksize=config.CHUNK_SIZE))
    pool.map(new_process, group)
    pool.close()
    pool.join()
    t_end = time.time()
    print('[over]-process use {}'.format(t_end-t_start))


if __name__ == '__main__':
    start('/Users/young/Desktop/水晶剑宴会.csv')
