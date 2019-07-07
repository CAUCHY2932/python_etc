# -*- coding:utf-8 -*-
from flask import Flask
from app.models.book import db
from flask_login import LoginManager
__author__ = 'young'

login_manager=LoginManager()
def create_app():
    app = Flask(__name__)
    # 路径本身
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)

    db.init_app(app)
    login_manager.init_app(app)
    with app.app_context():
        db.create_all(app=app)
    return app

# 线程隔离
def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)