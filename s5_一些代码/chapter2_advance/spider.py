# -*- coding:utf-8 -*-
"""
create by young on 2019-03-11 21:48 
"""

__author__ = 'young'

import requests

url = 'http://www.baidu.com/'
headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
resp = requests.get(url=url, headers=headers)

# print(resp)
#
# print(resp.status_code==200)

if resp.status_code==200:
    # resp.encoding='utf-8'
    resp.encoding=resp.apparent_encoding
    # print('请求成功')
    print(resp.text)


