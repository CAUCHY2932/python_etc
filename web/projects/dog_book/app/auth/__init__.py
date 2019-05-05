# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/5/5 10:22
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
from flask import Blueprint


auth = Blueprint('auth', __name__)


from . import views
