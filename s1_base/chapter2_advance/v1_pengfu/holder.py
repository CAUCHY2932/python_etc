# -*- coding:utf-8 -*-
"""
create by young on 2019-03-11 22:09 
"""

__author__ = 'young'


def holder_text(text, file_name):
    """
    :param text:
    :return: None
    """
    with open(file_name, 'a') as f:
        f.write(text)
    return None




