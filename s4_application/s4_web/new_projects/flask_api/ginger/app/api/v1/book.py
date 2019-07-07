# -*-encoding:utf-8 -*-
"""
    2019/4/20 4:21
    create by young
"""

from app.libs.redprint import Redprint
# from itsdangerous import TimedJSONWebSignatureSerializer as serial


api = Redprint('book')


@api.route('/', method=['GET'])
def book_index():
    return 'get book'


@api.route('', method=['POST'])
def create_book():
    return 'create book'
