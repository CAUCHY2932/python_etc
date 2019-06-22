# -*- coding:utf-8 -*-
"""
create by young on 2018-12-31 22:21 
"""

from app.libs.redprint import Redprint
__author__ = 'young'


api=Redprint('book')

@api.route('/get')
def get_book():
    return 'get book'

@api.route('/create')
def create_book():
    return 'create book'


