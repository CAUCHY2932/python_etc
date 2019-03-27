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
        "address": addr_str,
    }
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
    # province, city = [x for x in processd]
    chunk['province'], chunk['city'], chunk['district'] = [x[0] for x in processd], \
                                                          [x[1] for x in processd], \
                                                          [x[2] for x in processd]


def start(file_name):
    for chunk in pd.read_csv(file_name):
        new_process(chunk)


def split_test():
    import re
    import pandas as pd
    demo_dict = {'nihao': [90, 67, 56], 'woshi': [89, 67, 6], 'daichai': ['nihao899kl', 'nihao899kl', 'nihao899kl']}
    df = pd.DataFrame(demo_dict)

    process = lambda x: re.split('[0-9]', x)
    processed = list(map(process, df['daichai']))
    # print(processed[0])
    left, right = [x[0] for x in processed], [x[3] for x in processed]
    print(left)
    print(processed)  # [['nihao', '', '', 'kl'], ['nihao', '', '', 'kl'], ['nihao', '', '', 'kl']]
    # df['left'], df['right'] = processed[0], processed[1]
    # print(df)


if __name__ == '__main__':
    split_test()
