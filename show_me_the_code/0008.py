# -*- coding:utf-8 -*-

"""
    2019/4/4 16:25 by young
"""
"""
一个HTML文件，找出里面的正文

"""

def get_body(html_file_name):
    """
    传入一个html文件，正文内容
    :param html_file_name:
    :return:
    """
    with open(html_file_name, 'r') as f:
        fr = f.read()

    


