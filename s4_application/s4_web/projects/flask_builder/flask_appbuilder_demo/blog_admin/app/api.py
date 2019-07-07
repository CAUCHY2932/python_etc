# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/5/9 12:55
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
from flask_appbuilder.api import BaseApi, expose, rison
from . import appbuilder
from flask import request


class ExampleApi(BaseApi):
    """
    http://localhost:5000/api/v1/example/greeting
    http://localhost:5000/api/v1/example/greeting2

    """

    resource_name = 'example'

    @expose('/greeting')
    def greeting(self):
        return self.response(200, message="Hello")

    @expose('/greeting2', methods=['POST', 'GET'])
    def greeting2(self):
        if request.method == 'GET':
            return self.response(200, message="Hello (GET)")
        return self.response(201, message="Hello (POST)")

    @expose('/greeting3')
    @rison()
    def greeting3(self, **kwargs):
        """

        http://localhost:5000/api/v1/example/greeting3?q=(name:daniel)
        :param kwargs:
        :return:
        """
        if 'name' in kwargs['rison']:
            return self.response(
                200,
                message="Hello {}".format(kwargs['rison']['name'])
            )
        return self.response_400(message="Please send your name")


appbuilder.add_api(ExampleApi)
