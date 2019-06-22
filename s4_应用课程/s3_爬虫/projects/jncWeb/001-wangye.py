# -*-coding:utf-8-*-

import requests
import json
from lxml import etree

def get(url):
    headers={
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)",
    }
    response=requests.get(url=url, headers=headers)
    if response.status_code==200:
        response.encoding=response.apparent_encoding
        return response.text
    return None

def parseContent(html):
    treeHtml=etree.HTML(html)
    parseList=treeHtml.xpath('//div[@class="pdlr20 pdtb20"]//dt')
    a={}
    print(len(parseList))
    for item in parseList:
        # print(item)
        stationName=item.xpath('./strong/a/text()')[0]
        stationNum=item.xpath('./p/span/text()')[0]
        with open('004.csv', 'a+') as f:
            f.write('{},{}\n'.format(stationName,stationNum))
        # print(stationName, stationNum)
        a[stationName]=stationNum
    print(a)
    return a


# def writeToCsv(content):
#     text=json.dumps(content)
#     with open('003.txt','w', encoding='gbk') as f:
#         f.write(text)


def main():
    # pass
    # url=input("请输入你的网址：\n")
    url='https://energy.cngold.org/jyzwd_17.htm'
    html=get(url=url)
    content=parseContent(html=html)
    # writeToCsv(content)


if __name__ == '__main__':
    main()