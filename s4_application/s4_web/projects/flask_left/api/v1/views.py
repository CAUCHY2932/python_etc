# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/5/7 12:58
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
# from flask import render_template, make_response
from flask import jsonify, request

from api import db
from api.v1.models import ArticleModel
from . import v1
from .forms import ArticleForm, IdForm


@v1.route('/')
def index():
    return 'hello world'


@v1.route('/article', methods=['POST'])
def add_article():
    form = ArticleForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        article = ArticleModel(title=title, content=content)
        db.session.add(article)
        db.session.commit()
        return jsonify({'status': True,
                        'method': 'post'})
    return jsonify({'status': False,
                    'method': 'post'})


@v1.route('/article-all', methods=['GET'])
def list_article():
    articles = ArticleModel.query.all()
    if articles:
        return jsonify([{'title': article.title,
                         'content': article.content,
                         'id': article.id} for article in articles])

    return jsonify([])


@v1.route('/article', methods=['GET'])
def get_article_by_id():
    form = IdForm(request.args)
    if form.validate():

        article = ArticleModel.query.filter_by(id=form.id.data).first()
        if article:
            return jsonify({'title': article.title,
                            'content': article.content,
                            'id': article.id})
    return jsonify({})


@v1.route('/article', methods=['DELETE'])
def del_article():
    # 如果是?id=${id}这种使用表单验证，传参要要用request.args
    form = IdForm(request.args)
    if form.validate():

        article = ArticleModel.query.filter_by(id=form.id.data).first()
        if article:
            db.session.delete(article)
            db.session.commit()
            return jsonify({'delete_status': True,
                            'delete_id': article.id})

    return jsonify({'delete_status': False,
                    'delete_id': -1})


@v1.route('/article', methods=['PUT'])
def edit_article():
    # 如果是?id=${id}这种使用表单验证，传参要要用request.args
    form = IdForm(request.args)
    form_article = ArticleForm()
    if form.validate():
        if form_article.validate_on_submit():
            article = ArticleModel.query.filter_by(id=form.id.data).first()
            if article:
                article.title = form_article.title.data
                article.content = form_article.content.data
                db.session.commit()
                return jsonify({'update_status': True,
                                'update_id': article.id})

    return jsonify({'update_status': False,
                    'update_id': -1})
