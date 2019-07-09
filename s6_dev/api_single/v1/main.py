# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/7/9 14:55
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""

from flask import Blueprint


main = Blueprint('main', __name__)


@main.route('/')
def index():
    return 'hello'
