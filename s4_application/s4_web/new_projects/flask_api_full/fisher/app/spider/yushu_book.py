from app.libs.http import Http
from .persistence import MySQL
from app import cache


class YuShuBook:
    """
        鱼书API提供数据
    """
    per_page = 15
    # isbn_url = 'https://api.douban.com/v2/book/isbn/{}'
    # keyword_url = 'https://api.douban.com/v2/book/search?q={}&count={}&start={}'
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        self.total = 0
        self.books = []

    @cache.memoize(timeout=60)
    def search_by_isbn(self, isbn):
        """
            isbn搜索的结果可以被缓存
        """
        url = self.isbn_url.format(isbn)
        result = Http.get(url)
        self.__fill_single(result)

    def search_by_keyword(self, keyword, page):
        """
            keyword不缓存，意义不大
        """
        page = int(page)
        url = self.keyword_url.format(keyword, self.per_page, self.per_page * (page - 1))
        result = Http.get(url)
        self.__fill_collection(result)

    @property
    def first(self):
        return self.books[0] if self.total >= 1 else None

    def __fill_single(self, data):
        if data:
            self.total = 1
            self.books.append(data)

    def __fill_collection(self, data):
        self.total = data['total']
        self.books = data['books']


class YuShuBookOld:
    """
        鱼书API提供数据
    """
    per_page = 15
    # isbn_url = 'https://api.douban.com/v2/book/isbn/{}'
    # keyword_url = 'https://api.douban.com/v2/book/search?q={}&count={}&start={}'
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    @cache.memoize(timeout=60)
    def search_by_isbn(cls, isbn, persistence=False):
        """
            isbn搜索的结果可以被缓存
        """
        # url = cls.isbn_url
        book_model = MySQL.has_existed(isbn)
        if book_model:
            return book_model, 'from_mysql'

    @classmethod
    def get_book_from_api(cls, isbn, persistence=False):
        url = cls.isbn_url.format(isbn)
        # result = Http(url).get()
        result = Http(url).get()
        if result.get('code') == 2000:
            return {}, 'from_api'
        if persistence:
            book_model = MySQL.persistence_douban(result)
            return book_model, 'from_mysql'
        return result, 'from_api'

    @classmethod
    def search_by_keyword(cls, keyword, page):
        """
            keyword不缓存，意义不大
        """
        page = int(page)
        url = cls.keyword_url.format(keyword, cls.per_page, cls.per_page * (page - 1))
        result = Http(url).get()
        return result, 'from_api'
