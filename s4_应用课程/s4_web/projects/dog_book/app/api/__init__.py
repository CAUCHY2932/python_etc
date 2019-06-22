# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/5/5 17:26
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
from flask import Blueprint


api = Blueprint('api', __name__)

from . import authentication, posts, users, comments, errors
