# -*- coding:utf-8 -*-
"""
create by young on 2018-12-28 23:49 
"""
import requests
__author__ = 'young'
url = 'http://127.0.0.1:8901/book/search/9787108006660/1'

# url='http://www.baidu.com'
r=requests.get(url=url)
print(r)