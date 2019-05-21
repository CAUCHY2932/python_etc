# -*- encoding:utf-8 -*-
"""
    20190414 
    create by young
"""


from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired


class SearchForm(Form):
    q = StringField(validators=[Length(min=1, max=30, message=''), DataRequired()])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)
