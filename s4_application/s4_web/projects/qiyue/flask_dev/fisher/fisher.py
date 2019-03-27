# -*- coding:utf-8 -*-
__author__ = 'young'

# from flask import Flask
# # from config import DEBUG
# from helper import is_isbn_or_key
# from flask import make_response
# from yushu_book import YuShuBook
# from flask import jsonify
from app import create_app

app=create_app()


# @app.route('/')
# def index():
#     return 'hello'

# 像访问字典一样访问DEBUG

if __name__ == '__main__':
    # 生产环境 nginx+uwsgi，作为模块被加载，如果不加这句话，生产服务器启动时，加载这个模块后同样会启用flask内置的服务器
    app.run(debug=app.config['DEBUG'], port=8901)
