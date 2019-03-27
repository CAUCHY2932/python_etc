# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/4/24 9:43
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
from json import JSONEncoder as _JSONEncoder

from flask import Flask as _Flask
from flask_cache import Cache


cache = Cache(config={'CACHE_TYPE': 'simple'})


class JSONEncoder(_JSONEncoder):
    def default(self, o):
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return dict(o)
        # if isinstance(o, date):
        #     return o.strftime('%Y-%m-%d')
        # raise ServerError()


class Flask(_Flask):
    json_encoder = JSONEncoder


def register_blueprints(app):
    from app.web.movie import movie
    # from app.web.main import index
    app.register_blueprint(movie, url_prefix='/movie')
    # app.register_blueprint(movie)
    # app.register_blueprint(index)


def register_plugins(app):
    from app.models.base import db
    db.init_app(app)
    with app.app_context():
        db.create_all()


def create_app():
    # app = Flask(__name__, static_folder='app/static', static_url_path='')
    app = Flask(__name__)
    app.config.from_object('app.config.secure')

    # 注册flask-cache模块
    # cache.init_app(app)

    register_blueprints(app)
    register_plugins(app)
    return app






