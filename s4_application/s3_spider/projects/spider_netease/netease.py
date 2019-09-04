__author__ = 'young'

import requests


# 业务需求：输入关键词，搜索出歌曲，然后供人试听，并免费下载
# 爬虫，抓取网页内容，解析提取网页内容，清洗和持久化
# 开启多线程
# 定义http头

class Spider_netease:
    def __init__(self):
        self.keyword = ''
        self.songs = []  # 由元组组成的列表
        self.content = ''

    def _fetch_content(url, headers):
        r = requests.get(url, headers)
        if r.status_code == 200:
            r.encoding = r.apparent_encoding
            return r
        return None

    def _fetch_text(self, resp):
        if resp:
            return resp.text
        return None

    def _fetch_binary(self, resp):
        if resp:
            return resp.content
        return None

    def _fetch_json(self, resp):
        if resp:
            return resp.json()
        return None

    def _analysis(self):
        pass

    def _persistent(self):
        pass

    def go_crawl(self):
        pass


if __name__ == "__main__":
    pass
