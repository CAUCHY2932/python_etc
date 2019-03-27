# -*- coding=utf-8 -*-
"""
    2019/3/11 20:44
    author:young
"""
from younger import app


@app.route('/')
def index():
    return 'hello world!'
