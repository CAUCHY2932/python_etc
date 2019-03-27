# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/7/10 8:48
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
from werkzeug.exceptions import HTTPException
from flask import request, json


class APIException(HTTPException):
    code = 500
    msg = 'sorry, we made a mistake (*￣︶￣)!'
    error_code = 999

    def __init__(self, msg=None, code=None, error_code=None,headers=None):
        if code:
            self.code = code
        if error_code:
            self.error_code = error_code
        if msg:
            self.msg = msg
        super(APIException, self).__init__(msg, None)

    def get_body(self, environ=None):
        body = dict(
            msg=self.msg,
            error_code=self.error_code,
            request=request.method + '' + self.get_url_no_param()
        )

        text = json.dumps(body)

        return text

    def get_headers(self, environ=None):
        """

        :param environ:
        :return: list of headers
        """

        return [('Content-Type', 'application/json')]

    @staticmethod
    def get_url_no_param():
        full_path = str(request.full_path)
        main_path = full_path.split('?')
        return main_path[0]

