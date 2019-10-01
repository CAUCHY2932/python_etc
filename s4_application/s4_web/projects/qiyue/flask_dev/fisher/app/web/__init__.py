# -*- coding:utf-8 -*-
"""
created by young on 2018/12/25 11:40
"""
# from app.web import

from flask import Blueprint
web = Blueprint('web', __name__)

__author__ = 'young'


from app.web import book

# from app.web import user

from app.web import auth
from app.web import drift
from app.web import gift
from app.web import wish
from app.web import main

from app.web import passenger
from app.web import errors
from app.web import test
