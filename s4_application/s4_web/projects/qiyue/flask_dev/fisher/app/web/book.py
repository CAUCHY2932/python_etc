# -*- coding:utf-8 -*-

from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from flask import jsonify
from app.forms.book import SearchForm
import json
from flask import render_template,flash
from app.view_models.book import BookCollection, BookViewModel
__author__ = 'young'

# blueprint

from . import web
from flask import request
@web.route('/')
def index():
    return '<h1>welcome to our site!</h1>'


# 视图函数不应该放到入口文件内

@web.route('/book/search')
def search():
    form =SearchForm(request.args)
    books=BookCollection()
    if form.validate():
        q=form.q.data.strip()
        page=form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book=YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q,page)

        books.fill(yushu_book,q)
        # return json.dumps(books, default=lambda o:o.__dict__)

    else:
        flash('搜索的关键字不符合要求，请重新输入关键字')
        # return jsonify(form.errors)
    return render_template('search_result.html', books=books)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.first)
    return render_template('book_detail.html', book=book, wishes=[], gifts=[])

@web.route('/test')
def test():
    r={
        'age':18,
        'name':'小白',
    }
    flash('hello this is flash!', category='error')
    flash('hello bayue', category='warning')
    return render_template('test.html',data=r)


@web.route('/save_to_wish')
def save_to_wish():
    pass
