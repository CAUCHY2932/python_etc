# -*- coding:utf-8 -*-
"""
    create by young on 2018/12/29 16:36
"""

__author__ = 'young'


# 如果没有类的方法，就很像一个伪面向对象
# 如果一个类的下面的静态方法很多，
# 或者又很多可以被改写为静态方法的方法，很有可能是一个伪面向对象


class BookViewModel:
    def __init__(self,book):
        self.title=book['title']
        self.publisher=book['publisher']
        self.author='、'.join(book['author'])
        self.pages=book['pages']
        self.price=book['price']
        self.isbn = book['isbn']
        self.summary=book['summary']
        self.image=book['image']

    @property
    def intro(self):
        intros = filter(lambda x: True if x else False,
                        [self.author, self.publisher, self.price])
        return '/'.join(intros)
class BookCollection:
    def __init__(self):
        self.total=0
        self.books=[]
        self.keyword=''



    def fill(self, yushu_book, keyword):
        self.total=yushu_book.total
        self.keyword=keyword
        self.books=[BookViewModel(book) for book in yushu_book.books]






class _BookViewModel:

    @classmethod
    def package_single(cls, data, keyword):
        returned = {
            'book': [],
            'total': 0,
            'keyword': keyword,
        }
        if data:
            returned['total'] = 1
            returned['book'] = [cls._cut_book_data(data)]
        pass

    @classmethod
    def package_collection(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword,
        }
        if data:
            returned['total'] = len(data['books'])
            returned['books'] = [cls._cut_book_data(book) for book in data['book']]
        pass

    @staticmethod
    def _cut_book_data(data):
        book = {
            'title': data['title'],
            'author': '、'.join(data['author']),
            'publisher': data['publisher'],
            'pages': data['pages'],
            'price': data['price'],
            'summary': data['summary'],
            'image': data['image'],
        }
        return book
        # pass
