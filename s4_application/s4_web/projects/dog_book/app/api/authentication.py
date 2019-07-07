# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/5/5 17:28
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
from flask import g
from flask_httpauth import HTTPBasicAuth
# from .errors import unah
from app.models import User

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(email, password):
    if email == '':
        return False
    user = User.query.filter_by(email=email).first()
    if not user:
        return False
    g.current_user = user
    return user.verify_password(password)
