# coding: utf-8

import requests

url = ''
resp = requests.get(url)


if resp.status_code == 200:
    print('hello')
