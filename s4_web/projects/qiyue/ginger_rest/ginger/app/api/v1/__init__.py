# -*-encoding:utf-8 -*-
"""
    2019/4/20 4:32
    create by young
"""
from flask import Blueprint
from app.api.v1 import book, user, client


def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)
    user.api.register(bp_v1)
    book.api.register(bp_v1)
    client.api.register(bp_v1)
    return bp_v1
