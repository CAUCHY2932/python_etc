# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/4/24 11:32
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
import requests


class Http(object):

    @staticmethod
    def get(url, return_json=True):
        ret = requests.get(url)
        if ret.status_code == 200:
            return ret.json() if return_json else ret.text
        return {} if return_json else ''
