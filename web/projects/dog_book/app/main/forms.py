# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019-05-04 23:09
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    name = StringField('what\'s your name', validators=[DataRequired()])
    submit = SubmitField('submit')
