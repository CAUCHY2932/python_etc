# -*- coding:utf-8 -*-
"""
create by young on 2018-12-31 22:20 
"""
from flask import Blueprint
from app.api.v1 import user, book


__author__ = 'young'


def create_blueprint_v1():
    # from app.api.v1.book import api
    # from app.api.v1.book import api

    bp_v1=Blueprint('v1', __name__)
    # user.api.register()
    user.api.register(bp_v1,url_prefix='/user')
    book.api.register(bp_v1,url_prefix='/book')

    return bp_v1


# def register_redprints():
#      pass




