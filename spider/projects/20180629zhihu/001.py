# encoding:utf-8
import requests
from lxml import etree

url='https://www.zhihu.com/search?type=content&q=%E7%A7%A6%E8%B7%AF'
url2='https://zhihu-web-analytics.zhihu.com/api/v1/logs/batch'
headers={
    "authority":"zhihu-web-analytics.zhihu.com",
    "method":"POST",
    "path":"/api/v1/logs/batch",
    "scheme":"https",
    "accept":"*/*",
    "accept-encoding":"gzip, deflate, br",
    "accept-language":"zh-CN,zh;q=0.9",
    "content-encoding":"gzip",
    "content-length": "1436",
    "content-type":"application/x-protobuf",
    "origin": "https://www.zhihu.com",
    "referer":"https://www.zhihu.com/search?type=content&q=%E7%A7%A6%E8%B7%AF",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36",
    "x-za-batch-size": "3",
    "x-za-log-version": "2.3.71",
    "x-za-platform": "1",
    "x-za-product": "1",

}
ret=requests.post(url2,headers=headers)

ret.encoding='utf-8'

print(ret.text)
