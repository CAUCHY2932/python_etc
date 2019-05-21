# -*-encoding:utf-8 -*-
"""
    2019/4/20 0:57
    create by young
"""
from sqlalchemy.sql.functions import current_user

from app.web import web


@web.route('/gifts/book/<isbn>')
def save_to_gift(isbn):
    if current_user.can_save_to_list(isbn):
        pass
    pass
