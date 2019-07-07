import requests
from lxml import etree

def get_page_detail(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    # print(response.text)
    return response.text


url='http://search.saic.gov.cn/auto3743/auto3744/201802/t20180222_272431.html'


def parse_page_index(html):
    result=etree.HTML(html)
    title=result.xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div/p[1]/font/strong/text()')[0]
    content=result.xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div/p/text()')
    return title,content
html=get_page_detail(url)
title,content=parse_page_index(html)
print(title)
# print(content)
# str=''
for item in content:
    print(item)
    # str=str+item
    # str=str+str(item).split()
# print(str)


