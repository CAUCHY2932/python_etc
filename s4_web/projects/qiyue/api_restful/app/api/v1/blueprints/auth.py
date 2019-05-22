# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/4/24 9:39
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""


from flask import Blueprint


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return 'login layout'


@auth.route('/register', methods=['GET', 'POST'])
def register():
    pass


# @auth.route('/login', methods=['GET', 'POST'])
# def login():
#     pass


@auth.route('/login', methods=['GET', 'POST'])
def log_out():
    pass
