# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/5/7 12:02
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
from flask import Blueprint


v1 = Blueprint('v1', __name__)

from . import views
