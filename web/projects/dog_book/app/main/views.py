# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019-05-04 23:09
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
from flask_login import login_required, current_user

from app.decorators import admin_required
from ..models import User, Role, Permission, Post
from . import main
from .forms import NameForm, EditProfileForm, EditProfileAdminForm, PostForm
from datetime import datetime
from flask import session, url_for, render_template, redirect, flash, request, current_app, abort
from .. import db


# @main.route('/', methods=['GET', 'POST'])
# def index():
#     # name = None
#     form = NameForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(username=form.name.data).first()
#         if user is None:
#             user = User(username=form.name.data)
#             db.session.add(user)
#             db.session.commit()
#             session['known'] = False
#         else:
#             session['known'] = True
#         # old_name = session.get('name')
#         # if old_name is not None and old_name != form.name.data:
#         #     flash('look like you have change your name!')
#
#         session['name'] = form.name.data
#         form.name.data = ''
#         return redirect(url_for('main.index'))
#     return render_template('index.html',
#                            current_time=datetime.utcnow(),
#                            form=form, name=session.get('name'),
#                            known=session.get('known', False))


@main.route('/', methods=['GET', 'POST'])
def index():
    form = PostForm()
    if current_user.can(Permission.WRITE) and form.validate_on_submit():
        post = Post(body=form.body.data,
                    author=current_user._get_current_object())
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('.index'))

    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('index.html', form=form, posts=posts)


    # page = request.args.get('page', 1, type=int)
    # show_followed = False
    # if current_user.is_authenticated:
    #     show_followed = bool(request.cookies.get('show_followed', ''))
    # if show_followed:
    #     query = current_user.followed_posts
    # else:
    #     query = Post.query
    # pagination = query.order_by(Post.timestamp.desc()).paginate(
    #     page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
    #     error_out=False)
    # posts = pagination.items
    # return render_template('index.html', form=form, posts=posts,
    #                        show_followed=show_followed, pagination=pagination)


@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first()

    if user is None:
        abort(404)
    posts = user.posts.order_by(Post.timestamp.desc()).all()
    return render_template('user.html', user=user, posts=posts)


@main.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        db.session.add(current_user._get_current_object())
        db.session.commit()
        flash('Your profile has been updated.')
        return redirect(url_for('.user', username=current_user.username))
    form.name.data = current_user.name
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', form=form)


@main.route('/edit-profile/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_profile_admin(id):
    user = User.query.get_or_404(id)
    form = EditProfileAdminForm(user=user)
    if form.validate_on_submit():
        user.email = form.email.data
        user.username = form.username.data
        user.confirmed = form.confirmed.data
        user.role = Role.query.get(form.role.data)
        user.name = form.name.data
        user.location = form.location.data
        user.about_me = form.about_me.data
        db.session.add(user)
        db.session.commit()
        flash('The profile has been updated.')
        return redirect(url_for('.user', username=user.username))
    form.email.data = user.email
    form.username.data = user.username
    form.confirmed.data = user.confirmed
    form.role.data = user.role_id
    form.name.data = user.name
    form.location.data = user.location
    form.about_me.data = user.about_me
    return render_template('edit_profile.html', form=form, user=user)
