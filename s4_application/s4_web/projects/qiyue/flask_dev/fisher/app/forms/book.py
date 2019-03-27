# -*- coding:utf-8 -*-
from wtforms import Form, StringField,IntegerField
from wtforms.validators import Length,NumberRange
__author__ = 'young'

# 参数校验
class SearchForm(Form):

    q = StringField(validators=[Length(min=1, max=30)])
    page= IntegerField(validators=[NumberRange(min=1, max=99)], default=1)
