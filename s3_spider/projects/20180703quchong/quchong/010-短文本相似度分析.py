# 语音助手
# 2018-07-03
# coding:utf-8

import urllib.request
import json
from urllib.parse import urlencode
import requests
import ssl


def get_token(ak,sk):
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

def baidubce(text_1,text_2,access_token):
    base_url='https://aip.baidubce.com/rpc/2.0/nlp/v2/simnet'+'&'
    body={
        "text_1": text_1,
        "text_2": text_2,
    }
    data = {
        "access_token": access_token,
    }
    host=base_url+urlencode(data)
    # host=base_url
    request = urllib.request.Request(host)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = urllib.request.urlopen(request,body)
    content = response.read()
    score_data = json.loads(content)
    score_str = score_data['score']
    if (score_str):
        print(score_str)
        return score_str
    return None

def main():
    ak=''
    sk=''
    access_token=get_token(ak,sk)
    text_1=''
    text_2=''
    score=baidubce(text_1,text_2,access_token)
    print(score)

