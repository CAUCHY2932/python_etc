# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/4/24 14:43
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
from wtforms import Form, IntegerField, StringField
from wtforms.validators import Length, NumberRange


class SearchForm(Form):
    # id = IntegerField(validators=Length(min=1, max=64))
    q = StringField(validators=[Length(min=1, max=30)])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)
