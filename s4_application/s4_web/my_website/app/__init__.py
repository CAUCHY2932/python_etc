# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019-08-03 20:58
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def register_plugins(app):

    db.init_app(app=app)
    if app.config['SSL_REDIRECT']:
        from flask_sslify import SSLify
        sslify = SSLify(app=app)


def register_bps(app):
    from .api.views import api
    app.register_blueprint(api, url_prefix='/api')


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init__app(app)

    register_bps(app=app)
    register_plugins(app=app)

    return app
