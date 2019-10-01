# coding:utf-8

from app.spider.yushu_book import YuShuBook
from flask import jsonify
from app.libs.helper import is_isbn_or_key
from app.view_models.book import BookViewModel, BookCollection
from app.web import web
from flask import request
from app.forms.book import SearchForm


@web.route('/book/search')
def search():
    """

    q： 普通关键词
    page: 页数
    """
    # isbn 13
    # isbn 10个0到9个数字组成
    form = SearchForm(request.args)

    books = BookCollection()
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)

        yushu_book = YuShuBook()
        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
            # result = YuShuBook.search_by_isbn(q)
            # result = BookViewModel.package_single(result, q)
        else:
            yushu_book.search_by_isbn(q, page)
            # result = YuShuBook.search_by_key(q, page)
            # result = BookViewModel.package_collection(result, q)
        # 序列化
        books.fill(yushu_book, q)
        return jsonify(books)
    else:
        return jsonify(form.errors)


@web.route('/')
def main_page():
    return 'hello!'
