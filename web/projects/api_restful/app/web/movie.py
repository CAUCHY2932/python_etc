# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/4/24 14:32
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
from flask import Blueprint
from app.spider.get_movie import MovieGetter
from flask import jsonify
movie = Blueprint('movie', __name__)


@movie.route('/<q>')
def get(q):
    """
    根据q获取电影的实际信息
    :param q:
    :return:
    """
    mg = MovieGetter()
    mg.search_by_keyword(q=q)

    # return mg.detail['subjects']
    return jsonify(mg.detail)
