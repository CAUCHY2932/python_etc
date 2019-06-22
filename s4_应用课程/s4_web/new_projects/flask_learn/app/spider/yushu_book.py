# coding:utf-8


from app.libs.httper import Http
from flask import current_app


class YuShuBook:
    """
    类变量用来存储一些数据，不需要经常改变的内容
    面向对象
    描述特征，类变量，实例变量
    行为，方法
    一个类中有大量的可以用classmethod替换的方法，则是伪面向对象，面向对象是不成功的
    """
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'
    per_page = 15

    def __init__(self):
        self.total = 0
        self.books = []

    def search_by_isbn(self, isbn):
        """
        没有存储数据的话，如果返回回去，则是伪面向对象，
        我们应该把数据存储到对象
        定义初始化变量值，并将其返回的值赋给对象本身
        将最终数据存储到对象本身，
        但是如果存储的过多，会太具体化，影响我们通过其他途径获取数据的方式
        :param isbn:
        :return:
        """
        url = self.isbn_url.format(isbn)
        result = Http.get(url)
        self.__fill_single(result)

    def search_by_key(self, keyword, page=1):
        """
        self 可以取到类变量，访问变量的顺序
        :param keyword:
        :param page:
        :return:
        """
        url = self.keyword_url.format(keyword, current_app.config['PER_PAGE'], self.calculate_start(page))
        result = Http.get(url)
        self.__fill_collection(result)

    def __fill_single(self, data):
        if data:
            self.total = 1
            self.books.append(data)

    def __fill_collection(self, data):
        self.total = data['total']
        self.books = data['books']

    @staticmethod
    def calculate_start(page):
        return (page - 1) * current_app.config['PER_PAGE']
