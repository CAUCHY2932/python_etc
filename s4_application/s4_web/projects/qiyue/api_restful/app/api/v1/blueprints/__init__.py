# coding:utf-8
"""
    :author: young
    :DATE: 2019/4/24 9:38
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""

from flask import Flask


def create_app():
    app = Flask(__name__)
    register_all_blueprints(app)
    return app


def register_all_blueprints(app):
    from app.api.v1.blueprints import user
    from app.api.v1.blueprints.auth import auth
    from app.api.v1.blueprints.main import main
    app.register_blueprint(user, url_prefix='/user')
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(main, url_prefix='/main')
