# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/5/7 13:21
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Length


class ArticleForm(FlaskForm):
    title = StringField('标题', validators=[DataRequired(), Length(0, 64)])
    content = StringField('内容', validators=[DataRequired(), Length(0, 1024)])


class IdForm(FlaskForm):
    id = IntegerField('id', validators=[DataRequired()])

