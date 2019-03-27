# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/4/24 9:38
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""


from flask import Blueprint


main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
def index():
    return 'index layout'


@main.route('/error')
def error():
    return 'some error has happen!'
