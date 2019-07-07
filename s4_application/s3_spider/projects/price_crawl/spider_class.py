# -*- coding:utf-8 -*-
"""
created by young on 2018/12/25 17:11
"""

import requests
from lxml import etree
from collections import Iterable
import re


__author__ = 'young'

# 构造一个对象
class Crawl_price:
    """
        select a mode to choose a platform to crawl
        parse a  html
        give
    """

    @staticmethod
    def select_mode(link_list, site):
        """
            link:

        """
        for order_num, each_site in enumerate(link_list):
            if each_site in site:
                return order_num
        return -1

    @staticmethod
    def get_html_source_code(url):
        headers = {

        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            response.encoding = response.apparent_encoding
            return response.text
        return None

    @staticmethod
    def htmlish(html_text):
        obj = etree.HTML(html_text)
        return obj

    # def jij(self, oi):
    #     pass

    @staticmethod
    def regex_parse(pattern_mode, text):
        pattern = re.compile(pattern_mode, re.S)
        ret = re.search(pattern, text)
        if len(ret) == 0:
            return None
        ret = ret.group()
        if isinstance(ret, Iterable):
            ret = ret[0]
        return ret

    @staticmethod
    def write_to_file(file_name, str_target):
        with open(file_name, 'a+') as fob:
            fob.write(str_target + '\n')
