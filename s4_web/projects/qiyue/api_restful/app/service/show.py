# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/4/25 17:00
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
from sqlalchemy import func, desc

# from app import cache
from app.models.base import db, Movie
from app.view_model.movieModel import MovieViewModel


class MovieService:
    """
        Gift服务层
    """

    # @staticmethod
    # def get_wish_counts(gifts):
    #     book_isbn_list = [gift.isbn for gift in gifts]
    #     count_list = db.session.query(func.count(Wish.id), Wish.isbn). \
    #         filter(Wish.launched == False, Wish.isbn.in_(book_isbn_list),
    #                Wish.status == 1).group_by(Wish.isbn).all()
    #     return count_list

    @staticmethod
    # @cache.memoize(timeout=600)
    def recent():
        movie_list = Movie.query.order_by(
            desc(Movie.id)).limit(10).all()
        movies = [MovieViewModel().rencent_data(mov) for mov in movie_list]
        return movies
