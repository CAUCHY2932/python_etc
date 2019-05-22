# -*- coding:utf-8 -*-
"""
created by young on 2018/12/25 17:05
"""

"""
    import the require module
"""

from price_crawl import spider_class as spder
from price_crawl import setting

__author__ = 'young'


def main():
    crawl_spider = spder.Crawl_price()
    for item in setting['SITE_LIST']:
        html_text = crawl_spider.get_html_source_code(item)
        if html_text is None:
            continue  # 出口一：
        order_num = crawl_spider.select_mode(link_list=setting['LINK_LIST'], item)
        if order_num == -1:
            str_taget = ''
        else:
            obj = crawl_spider.htmlish(html_text)
            str_target = crawl_spider.regex_parse(pattern_mode, text)
        crawl_spider.write_to_file(str_taget)


if __name__ == '__main__':
    main()
