# coding:utf-8

import requests

def get_page_detail(url):
    headers={
        'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0',
    }
    respon=requests.get(url,headers=headers)
    if respon.status_code==200:
        respon.encoding="utf-8"
        print(respon.text)
    else:
        print('{}'.format('出错啦!'))

url='http://ai.datahoop.cn/details.html?207'
url2='https://webim.tim.qq.com/v1/group_open_long_polling_http_noauth_svc/get_msg?websdkappid=537048168&v=1.7.0&platform=10&tinyid=144115211274109720&a2=47933354d054a2ff4a7e08b483ed6bd273ff6f5d1d3610923452c5c4a742f99b3b503276ba7d6a5295d59bed35b756b7cb793f6b038a5ff4838501ae328eb6954684f7ee1c3a8e6e&contenttype=json&sdkappid=1400098018&accounttype=28307&apn=1&reqtime=1531708424'
get_page_detail(url)