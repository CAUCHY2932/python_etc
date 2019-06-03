# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/6/3 17:38
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""

import requests


def get_content(url, json=True):
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.json if json else resp.text
    return {} if json else ''
