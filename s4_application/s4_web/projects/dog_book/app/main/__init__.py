# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019-05-04 23:06
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
from flask import Blueprint

from ..models import Permission

main = Blueprint('main', __name__)

from . import views, forms


@main.app_context_processor
def inject_permission():
    return dict(Permission=Permission)
