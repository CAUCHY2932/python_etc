# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/7/9 14:55
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask.json import JSONEncoder as _JSONEncoder
# from datetime import date

# from libs.error_code import ServerError

db = SQLAlchemy()


# class JSONEncoder(_JSONEncoder):
#     def default(self, o):
#         if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
#             return dict(o)
#         if isinstance(o, date):
#             return o.strftime('%Y-%m-%d')
#         raise ServerError()
#
#
# class Flask(_Flask):
#     json_encoder = JSONEncoder


def create_app():
    """
    initial flask app and return the application
    """
    # init and import settings
    app = Flask(__name__)
    app.config.from_object('config')
    app.config.from_object('secure')
    # app.config.from_object('api.secure')

    register_bp(app)

    register_plugins(app)

    return app


def register_bp(app):
    from v1.main import main
    app.register_blueprint(main)


def register_plugins(app):
    db.init_app(app)
