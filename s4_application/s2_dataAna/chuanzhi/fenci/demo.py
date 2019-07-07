# -*- coding:utf-8 -*-

"""
    2019/4/2 16:41 by young
"""

import jieba as ja
import requests
from bs4 import BeautifulSoup


def extract_text(url):
    # 发送url请求并获取响应文件
    page_source = requests.get(url).content
    bs_source = BeautifulSoup(page_source, 'lxml')

    # parse all p label
    report_text = bs_source.find_all('p')

    text = ''
    for p in report_text:
        text += p.get_text()
        text += '\n'

    return text


def extract_text_2(url):
    page_source = requests.get(url).content
    bs_source = BeautifulSoup(page_source, 'lxml')

    report_text = bs_source.find_all('p')

    return '\n'.join([p.get_text() for p in report_text])


# print(extract_text(url_demo))
#
# print('-'*30)
#
# print(extract_text_2(url_demo))

# with open('./report.txt', 'w', encoding='utf-8') as f:
#     f.write(extract_text_2(url_demo))


def word_frequency(text):
    from collections import Counter
    # 返回所有分词后长度大于等于2的词的列表
    words = [word for word in ja.cut(text, cut_all=True) if len(word) >= 2]

    # counter 是一个简单的计数器，统计字符出现的个数
    # 分词后的列表将转化为字典
    c = Counter(words)

    for word_freq in c.most_common(10):
        word, freq = word_freq
        print(word, freq)


if __name__ == "__main__":
    url = 'http://www.gov.cn/premier/2017-03/16/content_5177940.htm'
    text = extract_text(url)
    word_frequency(text)
