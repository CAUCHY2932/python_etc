# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/7/9 14:55
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
from flask import Flask


def create_app():
    """
    initial flask app and return the application
    """
    # init and import settings
    app = Flask(__name__)
    app.config.from_object('config')
    # app.config.from_object('api.secure')

    register_bp(app)

    register_plugins(app)

    return app


def register_bp(app):
    from v1.main import main
    app.register_blueprint(main)


def register_plugins(app):
    pass
