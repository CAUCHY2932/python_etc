# -*- coding:utf-8 -*-
"""
create by young on 2018-12-31 22:08 
"""
from app.app import create_app
__author__ = 'young'


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
