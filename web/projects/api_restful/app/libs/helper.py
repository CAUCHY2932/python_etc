# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/4/25 10:06
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
from flask import jsonify

from app.spider.get_movie import MovieGetter
from app.view_model.movieModel import MovieViewModel


def is_key_or_id(q: str):
    """
        {
        "key": 0,
        "id": 1,
    }
    判断q是key还是id
    :param q:
    :return:
    """
    short_q = q.strip()
    if short_q.isdigit() and 0 <= len(short_q) <= 10:
        return 'id'
    return 'key'

#
# def get_data_by_id(id):
#     mg = MovieGetter()
#     mg.search_by_id(id)
#     movies = MovieViewModel()
#     movies.collection_data(mg.detail)
#     # return MysqlStorage.insert_to_mysql(id)
#     return jsonify({'items': movies.movies,
#                     'total': movies.total})
#
#
# def get_data_by_keyword(q):
#     mg = MovieGetter()
#     mg.search_by_keyword(q)
#     movies = MovieViewModel()
#     movies.collection_data(mg.detail)
#     # return MysqlStorage.insert_to_mysql(id)
#     return jsonify({'items': movies.movies,
#                     'total': movies.total})



