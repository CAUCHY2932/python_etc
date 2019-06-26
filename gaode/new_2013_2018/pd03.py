# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/6/26 16:31
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
import pandas as pd
import requests
import json


def request_from_gaode(addr_str):
    payload = {
        "key": "",
        "output": "json",
        "address": addr_str}
    base_gaode_url = ""
    resp = requests.get(base_gaode_url, payload)
    return resp.text if resp.status_code == 200 else "{}"


def package_data(addr):
    try:
        addr_json = json.loads(addr)
        if addr_json["status"] == "1":
            province = addr_json["geocodes"][0]["province"]
            city = addr_json["geocodes"][0]["city"]
            district = addr_json["geocodes"][0]["district"]
            return province, city, district
        return "", "", ""
    except Exception as e:
        print(e)
        return "", "", ""


def new_process(chunk):
    processd = list(map(package_data, chunk['宴会地址']))
    chunk['province'], chunk['city'], chunk['district'] = [x[0] for x in processd], \
                                                          [x[1] for x in processd], \
                                                          [x[2] for x in processd]
    chunk.to_csv('./003.csv', index=False, mode='a+')


def start(file_name):
    # header = None，会指定第一行为数据
    # 默认第一行为列名
    for chunk in pd.read_csv(file_name):
        new_process(chunk)


if __name__ == '__main__':
    pass
