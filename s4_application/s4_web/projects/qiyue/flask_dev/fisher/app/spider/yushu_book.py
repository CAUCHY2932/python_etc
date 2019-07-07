# -*- coding:utf-8 -*-
__author__ = 'young'

from app.libs.httper import HTTP
from flask import current_app


# 查询操作持久化，类似于爬虫

class YuShuBook:
    # 模型层
    # 在鱼书中不必存储查询信息
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'
    # total=0
    # books=[]
    def __init__(self):
        self.total = 0
        self.books = []

    # @classmethod
    def search_by_isbn(self, isbn):
        url = self.isbn_url.format(isbn)
        result = HTTP.get(url)
        self.__fill_single(result)
        # return result
        # pass
    # @classmethod
    def search_by_keyword(self, keyword, page=1):
        count = current_app.config['PER_PAGE']
        start = self.calculate_start(page)
        url = self.keyword_url.format(keyword, count, start)
        result = HTTP.get(url)
        self.__fill_collection(result)
        # return result
        # pass
    # @classmethod
    def __fill_single(self, data):
        if data:
            self.total = 1
            self.books.append(data)
            # self.books.append(data)
    # @classmethod
    def __fill_collection(self, data):
        self.total = data['total']
        self.books = data['books']
    @classmethod
    def calculate_start(self, page):
        return (page - 1) * current_app.config['PER_PAGE']

    @property
    def first(self):
        return self.books[0] if self.total >= 1 else None
