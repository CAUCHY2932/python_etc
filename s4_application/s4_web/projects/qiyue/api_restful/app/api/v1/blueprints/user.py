# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/4/24 9:26
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""

from flask import Blueprint


user = Blueprint('user', __name__)


@user.route('/', methods=['POST'])
def user_add():
    return 'user add'


@user.route('/', methods=['DELETE'])
def user_del():
    return 'user delete'


@user.route('/', methods=['PUT'])
def user_update():
    return 'user update'


@user.route('/', methods=['GET'])
def user_get():
    return 'user get'
