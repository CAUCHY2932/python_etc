# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/4/24 9:43
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
from flask import Flask


def register_blueprints(app):
    from app.web.movie import movie
    app.register_blueprint(movie, url_prefix='/movie')


def register_plugins(app):
    from app.models.base import db
    db.init_app(app)
    with app.app_context():
        db.create_all()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.secure')
    register_blueprints(app)
    # register_plugins(app)
    return app
