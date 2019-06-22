# -*- coding:utf-8 -*-
"""
create by young on 2019-03-11 22:08 
"""

__author__ = 'young'

from lxml import etree


def parser_text(html):
    """
    :parameter html obj
    :return: parsed obj
    """
    ret = etree.HTML(html)
    return ret

