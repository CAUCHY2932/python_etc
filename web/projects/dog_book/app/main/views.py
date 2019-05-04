# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019-05-04 23:09
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
from ..models import User
from . import main
from .forms import NameForm
from datetime import datetime
from flask import session, url_for, render_template, redirect
from .. import db


@main.route('/', methods=['GET', 'POST'])
def index():
    # name = None
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
        else:
            session['known'] = True
        # old_name = session.get('name')
        # if old_name is not None and old_name != form.name.data:
        #     flash('look like you have change your name!')

        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html',
                           current_time=datetime.utcnow(),
                           form=form, name=session.get('name'),
                           known=session.get('known', False))



