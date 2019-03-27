# coding:utf-8

import requests


# settings

url = 'https://so.gushiwen.org/search.aspx'

def req(url, v):
    payload = dict(value=v)
    resp = requests.get(url, params=payload)
    if resp.status_code == 200:
        return resp.text


if __name__ == "__main__":
    resp = req(url, "洛神赋")
    print(resp)
