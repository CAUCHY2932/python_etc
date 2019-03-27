# -*- coding:utf-8 -*-

"""
    2019/4/4 15:33 by young
"""
"""


你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，
假设内容都是英文，请统计出你认为每篇日记最重要的词
"""


def count_word(file_name):
    """
    传入文件，并输出词频topN
    :param file_name:
    :return:
    """
    with open(file_name, 'r') as f:
        fr = f.read()

    lines = fr.split(' ')
    # 遍历时改变遍历主体
    # 删除所有的空格内容
    line_new = lines.copy()
    for item in lines:
        if item == ' ':
            line_new.remove(item)
    dict_return = {}
    for item in line_new:
        dict_return[item] = dict_return[item]+1 if dict_return.get(item) else 1
    return dict_return


# 生成一个英文文档
def get_html(url):
    """
    给出一个url，生成一个html文档

    :param url:
    :return:
    """
    import requests
    resp = requests.get(url)

    if resp.status_code == 200:
        resp.encoding = resp.apparent_encoding
        return resp.text

def parse_html(text):
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(text, 'lxml')

    ret_value = [str(item.string) for item in soup.find_all('p')]
    # ret_value = soup.get_text()
    return '\n'.join(ret_value)


def write_to_file(fileName, content):
    """
    输入一个文件名和所需填写的内容
    :param fileName:
    :param content:
    :return:
    """
    with open(fileName,  'a+') as f:
        f.write(content+'\n')


def feq_calc(dict_content):
    new_dict = {}
    # 构造反向kv，注意，v有重复值，所以需要进行判别
    for k, v in dict_content:
        new_dict[v] = new_dict[v].append(k) if new_dict.get(v) else [k,]
    return new_dict
# 或者使用zip方法
"""
 python字典按照value进行排序

先说几个解决的方法，具体的有时间再细说

d = {'a':1,'b':4,'c':2}

字典是这个，然后要对字典按照value进行排序

方法一：

sorted(d.items(),key = lambda x:x[1],reverse = True)

方法二：

import operator
sorted(d.items(),key = operator.itemgetter(1))

方法三：

f = zip(d.values(),d.keys())
sorted(f)
//结果是 [(1, 'a'), (2, 'c'), (4, 'b')]

zip 之后，zip函数默认会对第一个元素进行排序的，如何取消排序？

"""

def go():
    url = 'http://www.chinadaily.com.cn/a/201904/04/WS5ca5549da3104842260b455b.html'
    html = get_html(url)
    parsed = parse_html(html)
    # print(parsed)
    write_to_file('./news.txt', parsed)

    demo = count_word('./news.txt')
    print(demo)




go()

