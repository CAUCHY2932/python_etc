# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/4/24 11:24
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
from flask import jsonify

from app.libs.http_service import Http


class MovieGetter(object):
    """

    调用豆瓣电影的api接口，并持久化至数据库
    """
    keyword_url = 'https://api.douban.com/v2/movie/search?q={}&start={}&count={}'
    id_url = 'https://api.douban.com/v2/movie/subject/{}'

    def __init__(self):
        self.total = 0
        self.subjects = []

    def search_by_keyword(self, q, start=0, count=10):
        url = self.keyword_url.format(q, start, count)
        self.collection_data(Http.get(url))

    def search_by_id(self, id):
        url = self.id_url.format(id)
        self.single_data(Http.get(url))

    def single_data(self, data):
        self.total = 1
        self.subjects = [data]

    def collection_data(self, data):
        self.total = data['total']
        self.subjects = data['subjects']

    @property
    def detail(self):
        return {
            'total': self.total,
            'subjects': self.subjects,
        }


if __name__ == '__main__':
    # mg = MovieGetter()
    # mg.search_by_keyword('海王')
    # print(mg.subjects)
    # print(result)
    pass
