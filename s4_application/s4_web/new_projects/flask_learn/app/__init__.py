# coding:utf-8

from flask import Flask
from app.models.book import db


def create_app():
    """
    创建app
    """
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)

    db.init_app(app)
    with app.app_context():
        db.create_all()
    # db.create_all(app=app) # 这里必须指定app=app,app则不行
    return app


def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)
