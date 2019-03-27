# coding:utf-8


import requests

resp = requests.get('http://www.baidu.com/')

if resp.status_code == 200:
    resp.encoding = resp
    print('hello')
