# -*-encoding:utf-8 -*-
"""
    2019/4/20 4:21
    create by young
"""

from app.libs.redprint import Redprint

api = Redprint('user')


@api.route('/<user>')
def get_usr(user):
    return 'hello {}'.format(user)


