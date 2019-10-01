# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/5/5 17:28
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
from flask import render_template, request, jsonify

from app.main import main


@main.app_errorhandler(404)
def page_not_found(e):
    if request.accept_mimetypes.accept_json and \
            not request.accept_mimetypes.accept_html:
        response = jsonify({'error': 'not found'})
        response.status_code = 404
        return response
    return render_template('404.html'), 404


def forbidden(message):
    response = jsonify({'error': 'forbidden'},
                       {'message': message})
    response.status_code = 403
    return response
