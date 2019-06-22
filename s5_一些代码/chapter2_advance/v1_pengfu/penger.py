# -*- coding:utf-8 -*-
"""
create by young on 2019-03-11 22:08 
"""
from chapter2_advance.v1_pengfu import configer
# import chapter2_advance.v1_pengfu.configer
__author__ = 'young'

import requests


# from . import configer

# 复用，抽象
# 获取源代码
def get_page_source(url):
    """
    :parameter url
    :return: obj
    """
    resp = requests.get(url=url, headers=configer.HEADERS)
    if resp.status_code == 200:
        resp.encoding = resp.apparent_encoding
        return resp.text
