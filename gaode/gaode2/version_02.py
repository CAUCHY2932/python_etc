# coding:utf-8
"""
author: young
datetime: 20190620
"""

import requests
import json

def request_from_baidu_map(addr):
    """
    地理编码
    input 地址信息
    return 包含经纬度的信息
        {
        "status": 0,
        "result": {
            "location": {
                "lng": 114.63559038099021,
                "lat": 33.49375247155689
            },
            "precise": 0,
            "confidence": 50,
            "comprehension": 68,
            "level": "道路"
        }
    }
    """

    url = "http://api.map.baidu.com/geocoder/v2/"

    querystring = {"address": addr, 
                   "output": "json",
                   "ak": ""}

    response = requests.request("GET", url, params=querystring)
    return response.text if response.status_code == 200 else ""


def parse_lat_and_lng_from_baidu(lat, lng):
    """
    地理逆编码
    input 输入经纬度
    return 包含具体地址和经纬度
        {
        "status": 0,
        "result": {
            "location": {
                "lng": 104.06744547494215,
                "lat": 30.68003767690029
            },
            "formatted_address": "四川省成都市青羊区王家塘街111号",
            "business": "新华西路,八宝街,江汉路",
            "addressComponent": {
                "country": "中国",
                "country_code": 0,
                "country_code_iso": "CHN",
                "country_code_iso2": "CN",
                "province": "四川省",
                "city": "成都市",
                "city_level": 2,
                "district": "青羊区",
                "town": "",
                "adcode": "510105",
                "street": "王家塘街",
                "street_number": "111号",
                "direction": "附近",
                "distance": "2"
            },
            "pois": [],
            "roads": [],
            "poiRegions": [],
            "sematic_description": "天象大厦附近37米",
            "cityCode": 75
        }
    }
    """
    base_url = 'http://api.map.baidu.com/geocoder/v2/'
    payload = {
        'location': '{},{}'.format(lat, lng),
        'ak': '',
        'output': 'json',
    }
    resp = requests.get(base_url, payload)
    return resp.text if resp.status_code == 200 else ""


def parse_addr(addr):
    """
    在线解析:
    https://www.json.cn/

    json格式样例
        {
        "status": 0,
        "result": {
            "location": {
                "lng": 104.06744547494215,
                "lat": 30.68003767690029
            },
            "formatted_address": "四川省成都市青羊区王家塘街111号",
            "business": "新华西路,八宝街,江汉路",
            "addressComponent": {
                "country": "中国",
                "country_code": 0,
                "country_code_iso": "CHN",
                "country_code_iso2": "CN",
                "province": "四川省",
                "city": "成都市",
                "city_level": 2,
                "district": "青羊区",
                "town": "",
                "adcode": "510105",
                "street": "王家塘街",
                "street_number": "111号",
                "direction": "附近",
                "distance": "2"
            },
            "pois": [],
            "roads": [],
            "poiRegions": [],
            "sematic_description": "天象大厦附近37米",
            "cityCode": 75
        }
    }
    
    返回结果包括：
    经度
    纬度
    省
    市
    区
    """
    addr_dict = json.loads(addr)
    if addr_dict.get('status', -1) == 0:
        lat = addr_dict["result"]["lat"]
        lng = addr_dict["result"]["lng"]
        province = addr_dict["result"]["addressComponent"]["province"]
        city = addr_dict["result"]["addressComponent"]["city"]
        district = addr_dict["result"]["addressComponent"]["district"]
    


def split_text():

    pass


def read_from_csv():
    pass


def test_detail_addr():
    addr = '商水县迎宾大道终端颐和酒店二楼包间'
    result = request_from_baidu_map(addr)
    print('{}的结果是：\n{}'.format(addr, result))


def test_lat_lng():
    lat, lng = '30.680037807006812', '104.06744547494219'
    addr = parse_lat_and_lng_from_baidu(lat, lng)
    print('{}, {}的结果是：\n{}'.format(lat, lng, addr))


if __name__ == '__main__':
    test_detail_addr()
    # test_lat_lng()
