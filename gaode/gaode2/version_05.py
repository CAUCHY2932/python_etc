# coding:utf-8
"""
author: young
datetime: 20190620
"""

import requests
import json


def request_from_baidu_map(addr):
    """
    接收详细地址，获取包含经纬度的字符串
    """
    url = "http://api.map.baidu.com/geocoder/v2/"

    querystring = {"address": addr,
                   "output": "json",
                   "ak": ""}

    response = requests.request("GET", url, params=querystring)
    return response.text if response.status_code == 200 else ""


def parse_lat_and_lng_from_baidu(lat, lng):
    base_url = 'http://api.map.baidu.com/geocoder/v2/'
    payload = {
        'location': '{},{}'.format(lat, lng),
        'ak': '',
        'output': 'json',
    }
    resp = requests.get(base_url, payload)
    return resp.text if resp.status_code == 200 else "" 


def parse_lng_and_lat(lng_lat_json):
    lat_lng_dict = json.loads(lng_lat_json)
    lat, lng = lat_lng_dict["result"]["location"]["lat"], lat_lng_dict["result"]["location"]["lng"]
    return lat, lng


def parse_addr(addr_json):
    addr_dict = json.loads(addr_json)
    if addr_dict.get('status', -1) == 0:
        lat = addr_dict["result"]["location"]["lat"]
        lng = addr_dict["result"]["location"]["lng"]
        province = addr_dict["result"]["addressComponent"]["province"]
        city = addr_dict["result"]["addressComponent"]["city"]
        district = addr_dict["result"]["addressComponent"]["district"]
        adcode = addr_dict["result"]["addressComponent"]["adcode"]
        formatted_address = addr_dict["result"]["formatted_address"]

        return lat, lng, province, city, district, adcode, formatted_address
    return ''


def split_text():

    pass


def read_from_csv(file_name, loop_num):
    with open(file_name, 'r') as f:
        line = f.readline()
        count = 1
        while line and count <= loop_num:
            yield line
            line = f.readline()
            count = count + 1


def record_to_file(record):
    id, addr = record.split(",")
    # hadle addr.strip()

    return id + "," + addr.strip()


if __name__ == '__main__':
    pass
