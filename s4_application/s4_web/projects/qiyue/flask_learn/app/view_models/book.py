# -*- coding:utf-8 -*-

"""
    2019/4/16 10:19 by young
"""


class BookViewModel(object):
    """
    包含单本数据
    """
    def __init__(self, book):
        self.title = book['title']
        self.publisher = book['publisher']
        self.image = book['image']
        self.price = book['price']
        self.summary = book['summary']
        self.pages = book['pages']


class BookCollection:
    """
    多本数据
    python不能直接序列化一个对象
    一个对象有可能是由其他对象组成的
    如何序列化一个对象
    """
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, yushu_book, keyword):
        """

        :param yushu_book:鱼书对象
        :param keyword:
        :return:
        """
        self.total = yushu_book.total
        self.keyword = keyword
        self.books = [BookViewModel(book) for book in yushu_book.books]


class _BookViewModel(object):
    """
    用于裁剪返回的数据格式
    """
    @classmethod
    def package_single(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword,
        }
        if data:
            returned['total'] = 1
            returned['books'] = [cls.__cut_book_data(data)]
        return returned

    @classmethod
    def package_collection(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword,
        }
        if data:
            returned['total'] = data['total']
            returned['books'] = [cls.__cut_book_data(book) for book in data['books']]
        return returned

    @classmethod
    def __cut_book_data(cls, data):
        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            'pages': data['pages'] or '',
            'author': '、'.join(data['author']),
            'price': data['price'],
            'summary': data['summary'],
            'image': data['image'],
            'isbn': data['isbn'],
        }
        return book
