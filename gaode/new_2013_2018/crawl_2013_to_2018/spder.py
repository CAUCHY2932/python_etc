# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/6/26 11:23
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
import pandas
import numpy as np
from .items import Items


class Crawler(object):
    name = 'myspider'
    start_requests = []

    def process(self):
        i = Items()
        i['province'] = '90'