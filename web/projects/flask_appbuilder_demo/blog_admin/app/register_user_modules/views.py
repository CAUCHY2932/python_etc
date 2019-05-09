# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/5/9 16:20
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""

from flask_appbuilder.security.registerviews import RegisterUserDBView
from flask_appbuilder.security.sqla.manager import SecurityManager
from flask_babel import lazy_gettext


class MyRegisterUserDBView(RegisterUserDBView):
    email_template = 'register_mail.html'
    email_subject = lazy_gettext('Your Account activation')
    activation_template = 'activation.html'
    form_title = lazy_gettext('Fill out the registration form')
    error_message = lazy_gettext('Not possible to register you at the moment, try again later')
    message = lazy_gettext('Registration sent to your email')


class MySecurityManager(SecurityManager):
    registeruserdbview = MyRegisterUserDBView
