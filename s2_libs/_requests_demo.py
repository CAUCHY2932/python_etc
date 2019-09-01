# coding: utf-8
import requests


def request_url(url):
    response=requests.get(url)
    if response.status_code==200:
        response.encoding=response.apparent_encoding
        print(response.text)
