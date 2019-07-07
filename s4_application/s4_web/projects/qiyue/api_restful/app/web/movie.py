# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/4/24 14:32
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
from flask import Blueprint, request, render_template

from app.forms.movie import SearchForm, IdForm
from app.libs.helper import is_key_or_id
# from app.libs.helper_1 import get_data
from app.service.show import MovieService
from app.spider.get_movie import MovieGetter
from flask import jsonify
from app.spider.persistence import MysqlStorage
from app.view_model.movieModel import MovieViewModel

movie = Blueprint('movie', __name__)


@movie.route('')
def get():
    """
    根据q获取电影的实际信息
    :return:
    """
    form = SearchForm(request.args)
    # MysqlStorage.is_exist(id)
    if form.validate():
        q = form.q.data.strip()
        mg = MovieGetter()
        if is_key_or_id(q) == 'id':
            mv = MysqlStorage.is_exist(q)
            if mv:
                return jsonify(mv)
            mg.search_by_id(q)
        else:
            mg.search_by_keyword(q=q)
        movies = MovieViewModel()
        movies.collection_data(mg.detail)
        result = {'items': movies.movies,
                  'total': movies.total}
        for item in result['items']:
            mv = MysqlStorage.is_exist(item['id'])
            if mv:
                return jsonify(mv)
            MysqlStorage.insert_to_mysql(item)
        return jsonify(result)
    return jsonify({})


@movie.route('/item/')
def get_item():
    form = IdForm(request.args)
    # MysqlStorage.is_exist(id)
    if form.validate():
        id = form.id.data
        mv = MysqlStorage.is_exist(id)
        if mv:
            return jsonify(mv)

        mg = MovieGetter()
        mg.search_by_id(id)
        movies = MovieViewModel()
        movies.collection_data(mg.detail)
        result = {'items': movies.movies,
                  'total': movies.total}
        MysqlStorage.insert_to_mysql(result['items'][0])
        return jsonify(result)
    return jsonify({})


@movie.route('/index')
def index():
    """
        首页视图函数
        这里使用了缓存，注意缓存必须是贴近index函数的
    """
    movie_list = MovieService.recent()
    # return render_template('index_new.html', recent=movie_list)
    return render_template('index.html')

@movie.route('')
def my_gifts():
    pass


@movie.route('')
def my_wish():
    pass


@movie.route('')
def pending():
    pass


@movie.route('')
def register():
    pass


@movie.route('')
def logout():
    pass


@movie.route('')
def login():
    pass


@movie.route('')
def personal_center():
    pass
