# -*- coding:utf-8 -*-
"""
create by young on 2019-03-11 22:22 
"""
from chapter2_advance.v1_pengfu import penger, parser, extracer, holder

__author__ = 'young'

if __name__ == "__main__":
    url = 'http://www.pengfue.com/'
    ret = penger.get_page_source(url=url)
    ret= parser.parser_text(ret)
    ret = extracer.extrace_html(ret)
    for item in ret:
        # print(item)
        # print(type(item))
        holder.holder_text(item+'\n', file_name='./223.txt')
        print('something has been write to the file.txt!')
        # print('-'*90)
    # print(ret)


