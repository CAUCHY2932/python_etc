# -*-encoding:utf-8 -*-
"""
    2019/4/20 7:08
    create by young
"""
from threading import Thread

from flask import current_app, render_template
from flask_mail import Message


def send_async_email(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            pass


def send_email(to, subject, template, **kwargs):
    msg = Message('[鱼书]' + subject,
                  sender='',
                  recipients=[to])
    msg.html = render_template(template, **kwargs)

    thr = Thread(target=send_async_email, args=[current_app, msg])
    thr.start()
