from app.view_models.trade import TradeInfo
from flask import render_template, flash, request
from flask_login import current_user

from . import web
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.forms.book import SearchForm
from app.view_models.book import BookViewModel, BookCollection

from app.models.gift import Gift
from app.models.wish import Wish

__author__ = '七月'


@web.route('/book/search', methods=['Get', 'POST'])
def search():
    """
        书籍检索
        不缓存，缓存的意义很小，反而会占用内存
    """
    form = SearchForm(request.args)
    books = BookCollection()
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            yushu_book = YuShuBook()
            yushu_book.search_by_isbn(q)
        else:
            yushu_book = YuShuBook()
            yushu_book.search_by_keyword(q, page)
        books.fill(yushu_book, q)
    else:
        flash('搜索的关键字不符合要求，请重新输入关键字')
    return render_template('search_result.html', books=books)


# @web.route('/book/search', methods=['Get', 'POST'])
def search_test():
    """
        书籍检索
        不缓存，缓存的意义很小，反而会占用内存
    """
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            data, from_where = YuShuBook.search_by_isbn(q)
            if from_where == 'from_api':
                view_model = BookViewModel.from_api(q, data)
            else:
                view_model = BookViewModel.single_book_from_mysql(q, data)
        else:
            data_from_api = YuShuBook.search_by_keyword(q, page)
            view_model = BookViewModel.from_api(q, data_from_api)
    else:
        flash('搜索的关键字不符合要求，请重新输入关键字')
    return render_template('search_result.html', books=view_model)


@web.route('/book/<isbn>/detail')
# @cache.cached(timeout=1800)
def book_detail(isbn):
    """
        1. 当书籍既不在心愿清单也不在礼物清单时，显示礼物清单
        2. 当书籍在心愿清单时，显示礼物清单
        3. 当书籍在礼物清单时，显示心愿清单
        4. 一本书要防止即在礼物清单，又在赠送清单，这种情况是不符合逻辑的

        这个视图函数不可以直接用cache缓存，因为不同的用户看到的视图不一样
        优化是一个逐步迭代的过程，建议在优化的初期，只缓存那些和用户无关的“公共数据"
    """
    has_in_gifts = False
    has_in_wishes = False
    # isbn_or_key = is_isbn_or_key(isbn)
    # if isbn_or_key == 'isbn':
    # 获取图书信息
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)

    if current_user.is_authenticated:
        # 如果未登录，current_user将是一个匿名用户对象
        if Gift.query.filter_by(uid=current_user.id, isbn=isbn,
                                launched=False).first():
            has_in_gifts = True
        if Wish.query.filter_by(uid=current_user.id, isbn=isbn,
                                launched=False).first():
            has_in_wishes = True

    book = BookViewModel(yushu_book.first)
    # if has_in_gifts:
    trade_wishes = Wish.query.filter_by(isbn=isbn, launched=False).all()
    trade_gifts = Gift.query.filter_by(isbn=isbn, launched=False).all()
    trade_wishes_model = TradeInfo(trade_wishes)
    trade_gifts_model = TradeInfo(trade_gifts)
    return render_template('book_detail.html', book=book, has_in_gifts=has_in_gifts,
                           has_in_wishes=has_in_wishes,
                           wishes=trade_wishes_model,
                           gifts=trade_gifts_model)
    # if has_in_wishes or (not has_in_gifts and not has_in_wishes):
    #     trade_gifts = Gift.query.filter_by(isbn=isbn, status=1, launched=False).all()
    #     trade_wishes_count = Wish.query.filter_by(isbn=isbn, launched=False,
    #                                               status=1).count()
    #     trade_gifts_model = GiftsViewModel.view_model_trade_info(trade_gifts)
    #     return render_template('book_detail.html', book=book, has_in_gifts=has_in_gifts,
    #                            has_in_wishes=has_in_wishes,
    #                            gifts=trade_gifts_model['trade'],
    #                            wishes_count=trade_wishes_count,
    #                            gifts_count=trade_gifts_model['total'])

    # trade_gifts_count = Gift.query.filter_by(isbn=isbn, launched=False, status=1).count()
    # trade_wishes_count = Wish.query.filter_by(isbn=isbn, launched=False, status=1).count()
    # return render_template('book_detail.html', book=book, has_in_gifts=has_in_gifts,
    #                        has_in_wish_list=has_in_wishes,
    #                        wishes_count=trade_wishes_count,
    #                        gifts_count=trade_gifts_count)
