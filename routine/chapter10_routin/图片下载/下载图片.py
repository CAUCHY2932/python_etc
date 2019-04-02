# coding:utf-8

import requests

url='http://jnc.fyun.online/JNC2017/?fileid=2018-10-20/201810201628431136.jpg&filename=X-YHBB20180934441136-1.jpg'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',

}
response=requests.get(url, headers=headers)


response.encoding=response.apparent_encoding

with open('./{}'.format('123.png'),'wb')as f:
    f.write(response.content)

