# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019-08-03 20:58
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
from flask import Blueprint

api = Blueprint('api', __name__)


@api.route('/')
def index():
    return 'hello'