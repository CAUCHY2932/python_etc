__author__='young'

import requests
from lxml import etree


# 业务需求：输入关键词，搜索出歌曲，然后供人试听，并免费下载
# 爬虫，抓取网页内容，解析提取网页内容，清洗和持久化
# 开启多线程
# 定义http头

class Spider_netease:
    def __init__:
        self.keyword=''
        self.songs=[] # 由元组组成的列表

    def _fetch_content(url,headers):
        r=requests.get(url,headers)
        if r.status_code==200:
            r.encoding=r.apparent_encoding
            return r
        return None

    def _fetch_text(resp):
        if resp:
            return resp.text
        return None

    def _fetch_binary(resp):
        if resp:
            return resp.content
        return None

    def _fetch_json():
        if resp:
            return resp.json
        return None

    def _analysis():
        pass

    def _persistent():
        pass


    def go_crawl():
        pass



if __name__=="__main__":
    pass