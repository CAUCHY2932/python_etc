# -*-encoding:utf-8 -*-
"""
    2019/4/20 23:41
    create by young
"""
from wtforms import Form, StringField, IntegerField
from wtforms.validators import DataRequired, length

from app.libs.enums import ClientTypeEnum


class ClientForm(Form):
    account = StringField(validators=[DataRequired(), length(min=5,  max=32)])
    secret = StringField()
    type = IntegerField()

    def validate_type(self, value):
        try:
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise e
