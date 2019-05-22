# -*- coding:utf-8 -*-
"""
create by young on 2018-12-31 22:21 
"""
from app.libs.redprint import Redprint
__author__ = 'young'

api=Redprint('user')

# @api.route('/', methods=['GET'])
# def get_user():
#     return 'get user'
#
# @api.route('/', methods=['PUST'])
# def create_user():
#     return 'create user'



@api.route('/get')
def get_user():
    return 'get user'

@api.route('/create')
def create_user():
    return 'create user'




# url不包含动词，
# 版本号加到url或是http头
# 理论是理论，实践是实践
# 内部开发，开放api 标准api内部使用不太方便，内部逻辑会很复杂
# 标准api粒度太粗
# 开放api，无需关注业务逻辑
# json 版本号
# 遵守rest，灵活，业务逻辑，接口