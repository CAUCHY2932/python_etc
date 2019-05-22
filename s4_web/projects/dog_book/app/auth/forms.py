# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/5/5 10:36
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, ValidationError

from app.models import User


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')


class RegisterForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField('Username',
                           validators=[DataRequired(),
                                       Length(1, 64),
                                       Regexp('^[A-Za-z0-9_.]*$',
                                              0,
                                              'Username must have only letters, numbers, dots or underscores')])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')
