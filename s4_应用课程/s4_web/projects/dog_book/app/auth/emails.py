# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/5/5 12:39
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
from flask_mail import Message
from flask import render_template

from app import mail
from config import Config

# FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
# FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'


def send_email(to, subject, template, **kwargs):
    msg = Message(Config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
                  sender=Config['FLASKY_MAIL_SENDER'],
                  recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)


