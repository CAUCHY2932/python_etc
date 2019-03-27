# coding:utf-8
# 手机号归属地查询

import requests
from lxml import etree


phoneNum=input('请输入一个手机号：\n')
url='http://www.ip138.com:8080/search.asp'
payload={
    'action':'mobile',
    'mobile':phoneNum,
}
response=requests.get(url,params=payload)
print('网址为:{}'.format(response.url))



if response.status_code==200:
    response.encoding=response.apparent_encoding
    # print(response.text)

html=etree.HTML(response.text)

try:
    retLst=html.xpath('//td[@class="tdc2"]/text()')
    # print(retLst)
    phone,location,cardType,areaCode,zipCode=retLst
    province,city=location.split()
    print('-'*40)
    print('手机：\t\t{}'.format(phone))
    print('省份：\t\t{}'.format(province))
    print('城市：\t\t{}'.format(city))
    print('地区：\t\t{}'.format(areaCode))
    print('邮政编码：\t{}'.format(zipCode))
    print('-'*40)

except Exception as e:
    print('find error:{}'.format(e))