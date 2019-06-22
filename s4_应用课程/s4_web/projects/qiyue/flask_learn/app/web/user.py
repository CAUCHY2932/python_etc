# -*-encoding:utf-8 -*-
"""
    20190414 22:26
    create by young
"""
from flask import request, redirect, url_for, render_template

from app.forms.register import RegisterForm
from app.models.user import User
from app.web import web


@web.route('/login')
def login():
    return render_template()
    pass


@web.route('/user/reg')
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User()
        user.set_attr(form.data)
        db.session.add(user)
        db.commit()
        redirect(url_for(endpoint='web.login'))
    pass
