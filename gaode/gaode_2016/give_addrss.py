# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/6/24 11:16
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
import requests
import json


def request_from_gaode(addr):
    payload = {
        "key": "",
        "output": "json",
        "address": addr,
    }
    base_gaode_url = "https://restapi.amap.com/v3/geocode/geo"
    resp = requests.get(base_gaode_url, payload)

    return resp.text if resp.status_code == 200 else ""


def parse_addr_json(addr):
    addr_json = json.loads(addr)
    try:
        if addr_json["status"] == "1":
            adcode = addr_json["geocodes"][0]["adcode"]
            citycode = addr_json["geocodes"][0]["citycode"]
            province = addr_json["geocodes"][0]["province"]
            city = addr_json["geocodes"][0]["city"]
            district = addr_json["geocodes"][0]["district"]
            lat_lng = addr_json["geocodes"][0]["location"]
            return 1, adcode, citycode, province, city, district, lat_lng
        return 0, "行政编码", "城市编码", "省", "市", "区", "经纬度"
    except Exception as e:
        print(e)
        return 0, "行政编码", "城市编码", "省", "市", "区", "经纬度"


def go():
    # func_list = [requests]
    addr = '安徽省芜湖市银湖路'
    addr_json = request_from_gaode(addr)
    print(addr, parse_addr_json(addr_json))


if __name__ == '__main__':
    go()
