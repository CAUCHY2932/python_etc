from wtforms import Form, StringField, IntegerField, PasswordField, ValidationError
from wtforms.validators import Length, NumberRange, DataRequired, Email
from app.models.user import User
__author__ = 'young'


class RegisterForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64), Email(message='电子邮箱不符合规范')])
    nickname = StringField('昵称', validators=[
        DataRequired(), Length(2, 10, message='昵称至少需要两个字符，最多10个字符')])

    password = PasswordField('密码', validators=[
        DataRequired(), Length(6, 20)])

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('昵称已存在')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮件已被注册')

# from wtforms import StringField, PasswordField, Form
# from wtforms.validators import Length, Email, \
#     ValidationError, EqualTo
# from .base import DataRequired
# from app.models.user import User
#
#
# class EmailForm(Form):
#     email = StringField('电子邮件', validators=[DataRequired(), Length(1, 64),
#                                             Email(message='电子邮箱不符合规范')])
#
#
# class ResetPasswordForm(Form):
#     password1 = PasswordField('新密码', validators=[
#         DataRequired(), Length(6, 20, message='密码长度至少需要在6到20个字符之间'),
#         EqualTo('password2', message='两次输入的密码不相同')])
#     password2 = PasswordField('确认新密码', validators=[
#         DataRequired(), Length(6, 20)])
#
#
# class ChangePasswordForm(Form):
#     old_password = PasswordField('原有密码', validators=[DataRequired()])
#     new_password1 = PasswordField('新密码', validators=[
#         DataRequired(), Length(6, 10, message='密码长度至少需要在6到20个字符之间'),
#         EqualTo('new_password2', message='两次输入的密码不一致')])
#     new_password2 = PasswordField('确认新密码字段', validators=[DataRequired()])
#
#
# class LoginForm(EmailForm):
#     password = PasswordField('密码', validators=[
#         DataRequired(message='密码不可以为空，请输入你的密码')])
#
#
# class RegisterForm(EmailForm):
#     nickname = StringField('昵称', validators=[
#         DataRequired(), Length(2, 10, message='昵称至少需要两个字符，最多10个字符')])
#
#     password = PasswordField('密码', validators=[
#         DataRequired(), Length(6, 20)])
#
#     def validate_email(self, field):
#         if User.query.filter_by(email=field.data).first():
#             raise ValidationError('电子邮件已被注册')
#
#     def validate_nickname(self, field):
#         if User.query.filter_by(nickname=field.data).first():
#             raise ValidationError('昵称已存在')
