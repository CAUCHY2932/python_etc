# 语音助手
# 2018-05-31
# coding:utf-8

import urllib.request
import json
from urllib.parse import urlencode
import requests
import ssl
# def get_token(ak,sk):
#
#     headers={
#         'Content-Type', 'application/json; charset=UTF-8'
#     }
#     base_url='https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&'
#     data={
#         'client_id':ak,
#         'client_secret':sk
#     }
#     url=base_url+urlencode(data)
#
#     response=requests.post(url,headers=headers)
#     content = response.text()
#     if (content):
#         print(content)
#         return content
#     return None


def get_token():
    ak=''
    sk=''
    base_url='https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&'
    data={
        'client_id':ak,
        'client_secret':sk
    }
    host=base_url+urlencode(data)
    request = urllib.request.Request(host)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = urllib.request.urlopen(request)
    content = response.read()
    token_data = json.loads(content)
    token_str = token_data['access_token']
    if (token_str):
        print(token_str)
        return token_str
    return None
# def
def baidubce():
    base_url='https://aip.baidubce.com/rpc/2.0/nlp/v2/simnet'

def main():
    access_token=get_token()


