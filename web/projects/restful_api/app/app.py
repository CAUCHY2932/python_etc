# -*- coding:utf-8 -*-
"""
create by young on 2018-12-31 22:09 
"""
from flask import Flask


__author__ = 'young'



def create_app():
    app=Flask(__name__)
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')
    register_blueprints(app)
    return app



def register_blueprints(app):
    from app.api.v1 import create_blueprint_v1
    # 这里为什么要带括号
    # app.register_blueprint(create_blueprint_v1())
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')

    # app.register_blueprint(book)
