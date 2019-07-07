# -*-encoding:utf-8 -*-
"""
    2019/4/20 23:39
    create by young
"""
from flask import request

from app.libs.enums import ClientTypeEnum
from app.libs.redprint import Redprint
from app.models.user import User
from app.validators.forms import ClientForm

api = Redprint('client')


@api.route('/register', method=['POST'])
def create_client():
    data = request.json
    form = ClientForm(data=data)
    if form.validate():
        promise = {
            ClientTypeEnum.USER_EMAIL: __register_user_by_email(),
            ClientTypeEnum.USER_MOBIL: __register_user_by_mobile(),
        }

    pass


def __register_user_by_email(form):
    User.register_by_email()
    pass


def __register_user_by_mobile():
    pass
