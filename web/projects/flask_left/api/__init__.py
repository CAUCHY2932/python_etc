# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/5/7 12:02
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
from flask import Flask
from flask_cors import CORS
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy

csrf = CSRFProtect()
db = SQLAlchemy()

def create_app():

    app = Flask(__name__)
    # app.config.from_object('config.py')

    # register plugins
    CORS(app, supports_credentials=True)
    csrf.init_app(app)
    db.init_app(app)

    # register blueprint
    from .v1 import v1 as v1_blueprint
    app.register_blueprint(v1_blueprint, url_prefix='/api/v1')

    return app

# initial index page
