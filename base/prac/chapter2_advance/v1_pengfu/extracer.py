# -*- coding:utf-8 -*-
"""
create by young on 2019-03-11 22:09 
"""

__author__ = 'young'


def extrace_html(html_obj):
    """
    :parameter HTML obj
    :return: extrace obj
    """
    # ret = html_obj.xpath('/html/body/div[1]/div[1]/div[1]/dl/dd/div[2]/text()')
    ret = html_obj.xpath('//div[@class="content-img clearfix pt10 relative"]/text()')
    if ret and len(ret)!=0:
        # ret_val = ret[0]
        return [item.strip() for item in ret]
    return None



