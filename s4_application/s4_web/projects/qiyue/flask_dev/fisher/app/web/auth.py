from . import web
from flask import render_template, request
from app.forms.auth import RegisterForm
from app.models.user import User
# from werkzeug.security import generate_password_hash
from app.models.base import db
from flask_login import login_user
__author__ = 'young'


@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User()
        user.set_attrs(form.data)
        db.session.add(user)
        db.session.commit()

    return render_template('auth/register.html', form={'data': {}})


@web.route('/login', methods=['GET', 'POST'])
def login():
    form=LoginForm(request.form)
    if request.method=='POST' and form.validate():
        user=User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user()
    pass


@web.route('/reget/password')
def forget_password_request():
    pass


@web.route('/reset/password/<token>')
def forget_password(token):
    pass
