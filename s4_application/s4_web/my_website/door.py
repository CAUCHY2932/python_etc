# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019-08-03 20:58
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
from app import create_app
import os


app = create_app(os.getenv('FLASK_CONFIG') or 'default')


if __name__ == '__main__':
    app.run()
