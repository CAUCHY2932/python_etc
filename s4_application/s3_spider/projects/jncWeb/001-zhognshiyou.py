# -*-coding:utf-8-*-

import requests
import json
from lxml import etree

def getHtml(url):
    headers={
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)",
    }
    response=requests.get(url=url, headers=headers)
    if response.status_code==200:
        response.encoding=response.apparent_encoding
        return response.text
    return None

def parseContent(html):
    # 打印加油站信息
    # print(html)
    treeHtml=etree.HTML(html)

    pageName=treeHtml.xpath('//div[@class="w680 fl"]/div[@class="mt20 border_top"]/div[@class="title clearfix"]/h2[@class="fl"]/a/text()')[0]
    print(pageName)
    parseList=treeHtml.xpath('//div[@class="pdlr20 pdtb20"]//dt')
    # a={}
    print(len(parseList))

# "/html/body/div[4]/div[1]/div[3]/div[1]/h2/a"

    for item in parseList:
        # print(item)
        stationName=item.xpath('./strong/a/text()')[0]
        stationNum=item.xpath('./p/span/text()')[0]
        with open('{}.csv'.format(pageName), 'a+') as f:
            f.write('{},{}\n'.format(stationName,stationNum))
        # print(stationName, stationNum)
    #     a[stationName]=stationNum
    # print(a)
    # return a


# def writeToCsv(content):
#     text=json.dumps(content)
#     with open('003.txt','w', encoding='gbk') as f:
#         f.write(text)



def parseList(url):
    """
    接受一个网址
    返回一个所有省份的列表
    :param url:
    :return:
    """
    a=getHtml(url=url)
    # '//div[@class="mt20 border_top"][1]//div[@class="country-cont"][1]/dl[1]//dd'
    Lst=etree.HTML(a)
    alst=Lst.xpath('//div[@class="mt20 border_top"][1]//div[@class="country-cont"][1]/dl[1]//dd/a/@href')
    # for item in alst:
    #     print(item)

    return alst




def main():
    # url='https://energy.cngold.org/jyzwd_17.htm'
    # html=getHtml(url=url)
    # content=parseContent(html=html)
    url='http://energy.cngold.org/jyzwd_cnpc.htm'
    provincelist=parseList(url=url)
    for item in provincelist:
        print(item)
        html=getHtml(item)
        parseContent(html)

if __name__ == '__main__':
    main()